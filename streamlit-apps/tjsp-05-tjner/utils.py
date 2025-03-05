import json
import numpy as np
import pandas as pd
import re
import torch

from pathlib import Path
from spacy.tokens import Doc, Span, Token
from spacy.language import Language
from torch import nn
from transformers import (
    AutoConfig,
    AutoTokenizer,
    AutoModelForSequenceClassification,
    AutoModelForTokenClassification,
)


START_TAG = "<START>"
STOP_TAG = "<STOP>"

# tag_to_ix = {
#     "<START>": 0,
#     "<STOP>": 1,
#     "O": 2,
#     "B-ORGAO_JULGADOR": 3,
#     "I-ORGAO_JULGADOR": 4,
#     "B-TITULO": 5,
#     "B-NOME_RECURSO": 6,
#     "I-NOME_RECURSO": 7,
#     "B-ORIGEM": 8,
#     "I-ORIGEM": 9,
#     "B-RECORRENTE": 10,
#     "I-RECORRENTE": 11,
#     "B-RECORRIDO": 12,
#     "I-RECORRIDO": 13,
#     "B-RESULTADO_ACORDAO": 14,
#     "I-RESULTADO_ACORDAO": 15,
#     "B-NOME_DESEMBARGADOR_MINISTRO": 16,
#     "I-NOME_DESEMBARGADOR_MINISTRO": 17,
#     "B-DATA": 18,
#     "I-DATA": 19,
#     "B-NOME_RELATOR": 20,
#     "I-NOME_RELATOR": 21,
#     "B-VOTO": 22,
#     "I-VOTO": 23,
#     "B-TEMA_KEYWORD": 24,
#     "I-TEMA_KEYWORD": 25,
#     "B-TEMA_RECURSO": 26,
#     "I-TEMA_RECURSO": 27,
#     "B-TEMA_COMPLEMENTO": 28,
#     "I-TEMA_COMPLEMENTO": 29,
# }

# ix_to_tag = {v : k for k, v in tag_to_ix.items()}

# with open(Path('assets', 'vocab.txt'), 'r', encoding='utf8') as f:
#     word_to_ix = { line.strip() : idx for idx, line in enumerate(f, start=4) }

def argmax(vec):
    # return the argmax as a python int
    _, idx = torch.max(vec, 1)
    return idx.item()

def prepare_sequence(seq, to_ix):
    idxs = [to_ix.get(w, 0) for w in seq]
    return torch.tensor(idxs, dtype=torch.long)


# Compute log sum exp in a numerically stable way for the forward algorithm
def log_sum_exp(vec):
    max_score = vec[0, argmax(vec)]
    max_score_broadcast = max_score.view(1, -1).expand(1, vec.size()[1])
    return max_score + \
        torch.log(torch.sum(torch.exp(vec - max_score_broadcast)))

MAX_LEN = 100  # Maximum length of sequences
EMBEDDING_DIM = 50  # Dimension of word embeddings

class BiLSTM_CRF(nn.Module):

    def __init__(self, vocab_size, tag_to_ix, embedding_dim, hidden_dim):
        super(BiLSTM_CRF, self).__init__()
        self.embedding_dim = embedding_dim
        self.hidden_dim = hidden_dim
        self.vocab_size = vocab_size
        self.tag_to_ix = tag_to_ix
        self.tagset_size = len(tag_to_ix)

        self.word_embeds = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(
            embedding_dim, hidden_dim // 2, num_layers=1, bidirectional=True
        )

        # Maps the output of the LSTM into tag space.
        self.hidden2tag = nn.Linear(hidden_dim, self.tagset_size)

        # Matrix of transition parameters.  Entry i,j is the score of
        # transitioning *to* i *from* j.
        self.transitions = nn.Parameter(torch.randn(self.tagset_size, self.tagset_size))

        # These two statements enforce the constraint that we never transfer
        # to the start tag and we never transfer from the stop tag
        self.transitions.data[tag_to_ix[START_TAG], :] = -10000
        self.transitions.data[:, tag_to_ix[STOP_TAG]] = -10000

        self.hidden = self.init_hidden()

    def init_hidden(self):
        return (
            torch.randn(2, 1, self.hidden_dim // 2),
            torch.randn(2, 1, self.hidden_dim // 2),
        )

    def _forward_alg(self, feats):
        # Do the forward algorithm to compute the partition function
        init_alphas = torch.full((1, self.tagset_size), -10000.0)
        # START_TAG has all of the score.
        init_alphas[0][self.tag_to_ix[START_TAG]] = 0.0

        # Wrap in a variable so that we will get automatic backprop
        forward_var = init_alphas

        # Iterate through the sentence
        for feat in feats:
            alphas_t = []  # The forward tensors at this timestep
            for next_tag in range(self.tagset_size):
                # broadcast the emission score: it is the same regardless of
                # the previous tag
                emit_score = feat[next_tag].view(1, -1).expand(1, self.tagset_size)
                # the ith entry of trans_score is the score of transitioning to
                # next_tag from i
                trans_score = self.transitions[next_tag].view(1, -1)
                # The ith entry of next_tag_var is the value for the
                # edge (i -> next_tag) before we do log-sum-exp
                next_tag_var = forward_var + trans_score + emit_score
                # The forward variable for this tag is log-sum-exp of all the
                # scores.
                alphas_t.append(log_sum_exp(next_tag_var).view(1))
            forward_var = torch.cat(alphas_t).view(1, -1)
        terminal_var = forward_var + self.transitions[self.tag_to_ix[STOP_TAG]]
        alpha = log_sum_exp(terminal_var)
        return alpha

    def _get_lstm_features(self, sentence):
        self.hidden = self.init_hidden()
        embeds = self.word_embeds(sentence).view(len(sentence), 1, -1)
        lstm_out, self.hidden = self.lstm(embeds, self.hidden)
        lstm_out = lstm_out.view(len(sentence), self.hidden_dim)
        lstm_feats = self.hidden2tag(lstm_out)
        return lstm_feats

    def _score_sentence(self, feats, tags):
        # Gives the score of a provided tag sequence
        score = torch.zeros(1)
        tags = torch.cat(
            [torch.tensor([self.tag_to_ix[START_TAG]], dtype=torch.long), tags]
        )
        for i, feat in enumerate(feats):
            score = score + self.transitions[tags[i + 1], tags[i]] + feat[tags[i + 1]]
        score = score + self.transitions[self.tag_to_ix[STOP_TAG], tags[-1]]
        return score

    def _viterbi_decode(self, feats):
        backpointers = []

        # Initialize the viterbi variables in log space
        init_vvars = torch.full((1, self.tagset_size), -10000.0)
        init_vvars[0][self.tag_to_ix[START_TAG]] = 0

        # forward_var at step i holds the viterbi variables for step i-1
        forward_var = init_vvars
        for feat in feats:
            bptrs_t = []  # holds the backpointers for this step
            viterbivars_t = []  # holds the viterbi variables for this step

            for next_tag in range(self.tagset_size):
                # next_tag_var[i] holds the viterbi variable for tag i at the
                # previous step, plus the score of transitioning
                # from tag i to next_tag.
                # We don't include the emission scores here because the max
                # does not depend on them (we add them in below)
                next_tag_var = forward_var + self.transitions[next_tag]
                best_tag_id = argmax(next_tag_var)
                bptrs_t.append(best_tag_id)
                viterbivars_t.append(next_tag_var[0][best_tag_id].view(1))
            # Now add in the emission scores, and assign forward_var to the set
            # of viterbi variables we just computed
            forward_var = (torch.cat(viterbivars_t) + feat).view(1, -1)
            backpointers.append(bptrs_t)

        # Transition to STOP_TAG
        terminal_var = forward_var + self.transitions[self.tag_to_ix[STOP_TAG]]
        best_tag_id = argmax(terminal_var)
        path_score = terminal_var[0][best_tag_id]

        # Follow the back pointers to decode the best path.
        best_path = [best_tag_id]
        for bptrs_t in reversed(backpointers):
            best_tag_id = bptrs_t[best_tag_id]
            best_path.append(best_tag_id)
        # Pop off the start tag (we dont want to return that to the caller)
        start = best_path.pop()
        assert start == self.tag_to_ix[START_TAG]  # Sanity check
        best_path.reverse()
        return path_score, best_path

    def neg_log_likelihood(self, sentence, tags):
        feats = self._get_lstm_features(sentence)
        forward_score = self._forward_alg(feats)
        gold_score = self._score_sentence(feats, tags)
        return forward_score - gold_score

    def forward(self, sentence):  # dont confuse this with _forward_alg above.
        # Get the emission scores from the BiLSTM
        lstm_feats = self._get_lstm_features(sentence)

        # Find the best path, given the features.
        score, tag_seq = self._viterbi_decode(lstm_feats)
        return score, tag_seq

class BiLSTMModel(nn.Module):
    def __init__(self,
                 vocab_size,
                 tagset_size,
                 embedding_dim,
                 hidden_dim,
                 num_layers
                ):
        super(BiLSTMModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim, padding_idx=0)
        self.lstm = nn.LSTM(embedding_dim,
                            hidden_dim,
                            num_layers=num_layers,
                            bidirectional=True,
                            batch_first=True)
        self.hidden2tag = nn.Linear(hidden_dim * 2, tagset_size)

    def forward(self, sentences):
        embeds = self.embedding(sentences)
        lstm_out, _ = self.lstm(embeds)
        tag_space = self.hidden2tag(lstm_out)
        tag_scores = nn.functional.log_softmax(tag_space, dim=2)
        return tag_scores

def pad_sequences(sequences, maxlen, padding='post', value=0):
    padded_sequences = np.full((len(sequences), maxlen), value)
    for i, seq in enumerate(sequences):
        if len(seq) > maxlen:
            if padding == 'post':
                padded_sequences[i, :maxlen] = seq[:maxlen]
            elif padding == 'pre':
                padded_sequences[i, -maxlen:] = seq[-maxlen:]
        else:
            if padding == 'post':
                padded_sequences[i, :len(seq)] = seq
            elif padding == 'pre':
                padded_sequences[i, -len(seq):] = seq
    return padded_sequences

def create_spans_from_labels(doc : Doc, labels : list):

    spans = []
    start = None
    current_label = None

    for i, label in enumerate(labels):
        if label == 'O':
            if start is not None:
                spans.append(Span(doc, start, i, label=current_label))
                start = None
                current_label = None
        elif label.startswith('B-'):
            if start is not None:
                spans.append(Span(doc, start, i, label=current_label))
            start = i
            current_label = label[2:]
        elif label.startswith('I-'):
            if start is not None and label[2:] == current_label:
                continue
            else:
                if start is not None:
                    spans.append(Span(doc, start, i, label=current_label))
                start = None
                current_label = None
        else:
            raise ValueError(f"Invalid label format: {label}")

    # Adiciona o último span, se houver
    if start is not None:
        spans.append(Span(doc, start, len(labels), label=current_label))

    return spans

class TJNerPipeline:

    def __init__(self, model, word2idx, tag2idx) -> None:
        self.model = model
        self.word2idx = word2idx
        self.tag2idx = tag2idx
        self.idx2tag = {v : k for k, v in tag2idx.items()}

        if not Doc.has_extension('predicted_labels'):
            Doc.set_extension('predicted_labels', default=None)

    @property
    def labels(self):
        label_gen = (k[2:] for k in self.tag2idx.keys() if k not in ['O', 'PAD'])
        return list(set(label_gen))

    def __call__(self, doc):
        print('Call TJ Ner Pipeline')
        word2idx = self.word2idx
        idx2tag = self.idx2tag
        model = self.model
        model.eval()

        sentences = [ [token.text for token in sent] for sent in doc.sents]
        X = [[word2idx.get(word, word2idx["UNK"]) for word in sentence] for sentence in sentences]
        X = pad_sequences(X, maxlen=MAX_LEN, padding="post")
        X = np.array(X)
        X = torch.tensor(X, dtype=torch.long)

        scores = model(X)
        preds = scores.argmax(dim=2).cpu().numpy()
        labels = np.vectorize(idx2tag.get)(preds)
        labels = pd.DataFrame(labels)
        tags = list()
        for i, row in labels.iterrows():
            ls = len(sentences[i])
            tag = row.tolist()[:ls]
            tags.extend(tag)

        doc._.predicted_labels = labels

        ents = create_spans_from_labels(doc, tags)
        doc.ents = ents

        return doc


@Language.factory('tjner')
def create_custom_ner_pipeline(nlp, name):
    best_model_filepath = Path('assets', 'best_model.pth')
    word2idx_filepath = Path('assets', 'word2idx.json')
    tag2idx_filepath = Path('assets', 'tag2idx.json')
    params_filepath = Path('assets', 'model_architecture.json')

    assert best_model_filepath.exists(), 'Cannot find the weights file'
    assert word2idx_filepath.exists(), 'Cannot find word2idx file'
    assert tag2idx_filepath.exists(), 'Cannot find tag2idx file'
    assert params_filepath.exists(), 'Cannot find model_architecture file'

    params = json.load(params_filepath.open())
    word2idx = json.load(word2idx_filepath.open())
    tag2idx = json.load(tag2idx_filepath.open())

    model = BiLSTMModel(**params)
    model.load_state_dict(torch.load(best_model_filepath))

    print(type(model))

    component = TJNerPipeline(model, word2idx=word2idx, tag2idx=tag2idx)

    return component

class WrapperBERTBasedNer:

    def __init__(self, model, tokenizer):
        self.model = model
        self.tokenizer = tokenizer
        self.tag2idx = model.config.label2id
        self.idx2tag = model.config.id2label

        if not Token.has_extension('is_valid'):
            Token.set_extension('is_valid', default=True)

    @property
    def labels(self):
        label_gen = (k[2:] for k in self.tag2idx.keys() if k not in ['O', 'PAD'])
        return list(set(label_gen))

    def __call__(self, doc):

        model = self.model
        tokenizer = self.tokenizer
        id2label = model.config.id2label
        max_length = 512

        # Realizar a etapa de predição

        # existe uma razão para não usar a função str.split aqui
        # a função str.split some com os caracteres em branco como espaço e \n
        # isso dificulta o alinhamento do texto e da sequência ao final do
        # procedimento
        batch = [ [t.text for t in sent] for sent in doc.sents]

        tokens = tokenizer(
                            batch,
                            return_tensors="pt",
                            truncation=True,
                            padding=True,
                            max_length=max_length,
                            is_split_into_words=True
                        )

        model.eval()

        with torch.no_grad():
            outputs = model(**tokens)

        preditions = torch.argmax(outputs.logits, dim=2)

        n_batches, n_sequence = preditions.shape

        print('# 1', n_batches, n_sequence)

        # = = = = = = = = = = = = = = = = = = = = = = = = =
        # 2 Decodificar a informação das predições

        preds = preditions.cpu().numpy()

        word_list = list()
        label_list = list()

        for i_batch in range(n_batches):
            current_word = ''
            current_id = None
            current_label = ''

            for id, token, idx_label in zip(tokens.word_ids(i_batch), tokens.tokens(i_batch), preds[i_batch]):

                if id == None:
                    continue

                if current_id == id:
                    current_word += token[2:] if token.startswith('##') else token

                else:
                    if current_id != None:
                        word_list.append(current_word)
                        label_list.append(current_label)

                    current_word = token
                    current_label = id2label[idx_label]
                    current_id = id

            if current_word and current_label:
                word_list.append(current_word)
                label_list.append(current_label)

        print('# 2', len(label_list), len(word_list))

        total_words = 0
        for _ in doc: total_words += 1
        print('# 3 :->', total_words)

        all_words = set(word_list)

        for t in doc:
            t._.is_valid = t.text in all_words

        total_valid = sum(t._.is_valid for t in doc)
        print('# 4', total_valid)

        for t in doc:
            if t._.is_valid and (t.text not in all_words):
                print(t.text)

        i_next = 0
        aligned_labels = list()

        unk_token = tokenizer.unk_token

        for t in doc:
            if t._.is_valid :
                # print(t.text, word_list[proximo], label_list[proximo])
                aligned_labels.append(label_list[i_next])
                i_next += 1
            else :
                txt = re.sub(r'\s+', '', t.text)
                if txt :
                    # print('\t*', txt, word_list[proximo], label_list[proximo])
                    aligned_labels.append(label_list[i_next])
                    i_next += 1
                else:
                    i = i_next if i_next < len(label_list) else len(label_list) - 1
                    local_label = label_list[i] if label_list[(i - 1)][2:] == label_list[i][2:] else 'O'
                    aligned_labels.append(local_label)
                    # print(t.text, local_label)

        print('# 5 :->', len(aligned_labels))

        spans = create_spans_from_labels(doc, aligned_labels)
        doc.ents = spans

        return doc


@Language.factory('NerBert')
def create_custom_bert_based_ner_pipeline(nlp, name):

    # caminho até o modelo
    model_path = Path('assets', 'bertimbau-cased-tjner')
    # model_path = "giliardgodoi/bertimbau-cased-tjner"

    config = AutoConfig.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path, config=config)
    model = AutoModelForTokenClassification.from_pretrained(model_path, config=config)

    return WrapperBERTBasedNer(model, tokenizer)