import pandas as pd
import re
import streamlit as st
import spacy
import utils # type: ignore #

from io import StringIO
from spacy import displacy
from pathlib import Path
from zipfile import ZipFile

st.set_page_config(
    page_title="Analisa Acórdãos",
    page_icon=":bookmark_tabs:",
    layout='wide',
    initial_sidebar_state='expanded'
)

options = {
    'ents': [
        'ORGAO_JULGADOR', 'TITULO', 'NOME_RECURSO', 'ORIGEM', 'RECORRENTE',
        'RECORRIDO', 'RESULTADO_ACORDAO', 'NOME_DESEMBARGADOR_MINISTRO', 'DATA',
        'NOME_RELATOR', 'VOTO', 'TEMA_KEYWORD', 'TEMA_RECURSO', 'TEMA_COMPLEMENTO'
    ],
    'colors': {
        'ORGAO_JULGADOR': 'linear-gradient(90deg, #aa9cfc, #fc9ce7)',
        'TITULO': 'linear-gradient(90deg, #ff9a9e, #fad0c4)',
        'NOME_RECURSO': 'linear-gradient(90deg, #fbc2eb, #a6c1ee)',
        'ORIGEM': 'linear-gradient(90deg, #ffecd2, #fcb69f)',
        'RECORRENTE': 'linear-gradient(90deg, #a1c4fd, #c2e9fb)',
        'RECORRIDO': 'linear-gradient(90deg, #d4fc79, #96e6a1)',
        'RESULTADO_ACORDAO': 'linear-gradient(90deg, #84fab0, #8fd3f4)',
        'NOME_DESEMBARGADOR_MINISTRO': 'linear-gradient(90deg, #fccb90, #d57eeb)',
        'DATA': 'linear-gradient(90deg, #e0c3fc, #8ec5fc)',
        'NOME_RELATOR': 'linear-gradient(90deg, #f093fb, #f5576c)',
        'VOTO': 'linear-gradient(90deg, #4facfe, #00f2fe)',
        'TEMA_KEYWORD': 'linear-gradient(90deg, #43e97b, #38f9d7)',
        'TEMA_RECURSO': 'linear-gradient(90deg, #fa709a, #fee140)',
        'TEMA_COMPLEMENTO': 'linear-gradient(90deg, #30cfd0, #330867)'
    }
}

MODELOS_NER_DISPONIVEIS = [
    'tjner',
    'NerBert'
]


@st.cache_resource
def get_spacy_model(pipename='tjner'):

    assert pipename in MODELOS_NER_DISPONIVEIS, 'O modelo solicitado não está entre os existentes'

    # nlp = spacy.load('pt_core_news_lg')
    nlp = spacy.blank('pt')
    nlp.add_pipe('sentencizer')
    nlp.add_pipe(pipename, last=True)

    return nlp


def ui_show_text_named_entities(nlp, doc, ner_pipeline):

    pipe = nlp.get_pipe(ner_pipeline)
    labels = pipe.labels

    with st.expander('Options'):
        selected_labels = st.multiselect('Labels', options=labels, default=labels)

    options["ents"] = selected_labels

    html = displacy.render([doc], style='ent', options=options)
    # html = re.sub("\s{2,}", " ", html)
    html = re.sub("\n", " ", html)
    # st.success("Visualizar conteudo")
    # prosecute_number = re.sub("(\d{7})(\d{2})(\d{4})(\d{1})(\d{2})(\d{4}).txt" ,
    #                           r"\1-\2.\3.\4.\5.\6", prosecute_number)
    # title = f"Processo número: {prosecute_number}"
    # st.header(title)
    st.write(html, unsafe_allow_html=True)


def main():

    with st.sidebar:
        st.header('Visualizador Entidades Nomeadas')

        pipename = st.selectbox(
            'Selecione o modelo:',
            options=MODELOS_NER_DISPONIVEIS
        )

    nlp = get_spacy_model(pipename=pipename)

    st.header(':bookmark_tabs: Visualizador de Entidades Nomeadas')

    uploaded_file = st.file_uploader('Subir arquivo')

    if uploaded_file is not None:

        content = StringIO(uploaded_file.getvalue().decode('utf8')).read()

        content = re.sub(r'\s+', ' ', content)

        doc = nlp(content)

        ui_show_text_named_entities(nlp, doc, pipename)

        st.write(doc._.predicted_labels)



if __name__ == '__main__':

    main()