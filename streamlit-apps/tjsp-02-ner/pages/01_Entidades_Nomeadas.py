from collections import defaultdict
import numpy as np
import pandas as pd
import re
import spacy
import streamlit as st

from pathlib import Path
from spacy import displacy
from zipfile import ZipFile
# from spacy_streamlit import visualize_ner

st.set_page_config(
    page_title="Analisa Acórdãos",
    page_icon=":bookmark_tabs:",
    layout='wide',
    initial_sidebar_state='expanded'
)

if 'zip-archive' not in st.session_state:
    archive = ZipFile(Path('..', 'data', 'documents-archive.zip'), mode='r')
    st.session_state['zip-archive'] = archive
    st.session_state['all-files'] = archive.namelist()

if 'frame' not in st.session_state :
    st.session_state['frame'] = None

label_prosecute_number = 'numero_processo'
label_for_document_content = 'conteudo'

colors = {"JURISPRUDENCIA": "#F2464F",
          "LEGISLACAO": "#00FF00",
          "TEMPO": "#F4A460",
          "LOCAL": "#FF6EFF", # 
          "PESSOA": "#FFD700",
          "ORGANIZACAO": "#00FFFF"}

options = {"ents": list(colors.keys()), "colors": colors}

@st.cache_data
def load_data(filepath : Path, **kwargs):
    if not issubclass(type(filepath), Path):
        raise RuntimeWarning(type(filepath))
    
    if '.parquet' in filepath.suffixes:
        df = pd.read_parquet(filepath, **kwargs)
    elif '.csv' in filepath.suffixes:
        df = pd.read_csv(filepath, **kwargs)
    elif ('.xlsx' in filepath.suffixes) or ('.xls'):
        df = df.read_excel(filepath, **kwargs)

    return df

@st.cache_resource
def get_spacy_model():
    # nlp = spacy.load(Path("lener_model", "model-best"))
    nlp = spacy.load("pt_core_news_lg")
    return nlp

def get_document_content(proscecute_code):
    archive = st.session_state['zip-archive']
    content = archive.read(proscecute_code)
    text = str(content, 'utf-8')   
    return text


def ui_show_text_named_entities(prosecute_number, doc):
    html = displacy.render([doc], style='ent', options=options)
    # html = re.sub("\s{2,}", " ", html)
    html = re.sub("\n", " ", html)
    st.success("Visualizar conteudo")
    prosecute_number = re.sub("(\d{7})(\d{2})(\d{4})(\d{1})(\d{2})(\d{4}).txt" , 
                              r"\1-\2.\3.\4.\5.\6", prosecute_number)
    title = f"Processo número: {prosecute_number}"
    st.header(title)
    st.write(html, unsafe_allow_html=True)
    

def ui_show_entity_table(frame : pd.DataFrame):        
        #ORG, PESSOA, LOCAL, JURIS, LEGIS, TEMPO
        ORG, PESSOA, LOCAL, JURIS, LEGIS, TEMPO = st.tabs([
            'Organização',
            'Pessoa', 
            'Local',
            'Jurisprudência',
            'Legislação',
            'Tempo'
        ])

        with ORG :
            df = frame.loc[lambda d: d['label'] == 'ORGANIZACAO']['Entidades']
            st.dataframe(df, use_container_width=True)
        
        with PESSOA:
            st.dataframe(frame.loc[lambda d: d['label'] == 'PESSOA']['Entidades'], 
                            use_container_width=True,
                        )
        
        with LOCAL:
            st.dataframe(frame.loc[lambda d: d['label'] == 'LOCAL']['Entidades'], 
                            use_container_width=True
                        )
        
        with JURIS:
            st.dataframe(frame.loc[lambda d: d['label'] == 'JURISPRUDENCIA']['Entidades'], 
                            use_container_width=True
                        )
        
        with LEGIS:
            st.dataframe(frame.loc[lambda d: d['label'] == 'LEGISLACAO']['Entidades'], 
                            use_container_width=True
                        )
        
        with TEMPO:
            st.dataframe(frame.loc[lambda d: d['label'] == 'TEMPO']['Entidades'], 
                            use_container_width=True
                        )

# identifica como header o texto que se repete no início de páginas seguidas
def detectHeader(s1,s2, minHeaderLen = 15):
            i = 0
            n1 = len(s1)
            n2 = len(s2)
            j = minHeaderLen
            while(j < n1):
                seq = s1[i:j]
                k = s2.find(seq)
                if k != -1:
                    k += minHeaderLen
                    while j < n1 and k < n2 and s1[j] == s2[k]:
                        j += 1
                        k += 1
                    return s1[i:j]
                i += 1
                j += 1
            return ''

# identifica como footer o texto que se repete no final de páginas seguidas
def detectFooter(s1, s2, minFooterLen = 15):
        n1 = len(s1)
        i = n1 - minFooterLen
        j = n1
        while(i >= 0):
            seq = s1[i:j]
            k = s2.rfind(seq)
            if k != -1:
                i -= 1
                k -= 1
                while i >= 0 and k >= 0 and s1[i] == s2[k]:
                    i -= 1
                    k -= 1
                footer = s1[(i+1):j]
                res = re.search(r'\n\s*\n',footer)
                if res:
                    return footer[res.start():]
                return ''
            i -= 1
            j -= 1
        return ''

# remove cabeçalho e rodapé do texto, baseado na igualdade destes entre páginas.
# as páginas devem ter separador, que será removido no fim do processo.
def removeHeaderFooter(text, pageSep='\x0c', maxHeaderLen=200, maxFooterLen=200):
        
        v = re.split(pageSep,text)
        pattern = ''
        numPages = len(v)
        for i in range(numPages):
            if i + 1 < numPages:
                page0 = ''.join([c for c in v[i] if c != ' ' and c != '\n'])
                page1 = ''.join([c for c in v[i+1] if c != ' ' and c != '\n'])
                end0 = maxHeaderLen
                end1 = maxHeaderLen
                if end0 > len(page0): end0 = len(page0)
                if end1 > len(page1): end1 = len(page1)
                header = detectHeader(page0[:end0],page1[:end1])
                if header:
                    pattern = r'\s*'.join(header)
            if pattern:
                try:
                    res = re.search(pattern,v[i])
                    if res and res.end() < maxHeaderLen:
                        v[i] = v[i][res.end():]
                except:
                    pass
        pattern = ''
        for i in range(numPages):
            if i + 1 < numPages:
                page0 = ''.join([c for c in v[i] if c != ' '])
                page1 = ''.join([c for c in v[i+1] if c != ' '])
                begin0 = len(page0) - maxFooterLen
                begin1 = len(page1) - maxFooterLen
                if begin0 < 0: begin0 = 0
                if begin1 < 0: begin1 = 0
                footer = detectFooter(page0[begin0:],page1[begin1:])
                if footer:
                    footer = footer.strip()
                    pattern = r'\s*'.join(footer)
            if pattern:
                try:
                    iter_res = re.finditer(pattern,v[i])
                    res = [m for m in iter_res]
                    if len(res) > 0:
                        if(len(v[i]) - res[-1].start() < maxFooterLen):
                            v[i] = v[i][:res[-1].start()]
                except:
                    pass
        return ' '.join(v)


def preprocessing(text):

    formatted_text = removeHeaderFooter(text)
    formatted_text = re.sub("\n\s+", '\n', formatted_text)
    formatted_text = re.sub('\x0c', ' ', formatted_text)
    formatted_text = re.sub('\n{2,}', '\n', formatted_text)
    formatted_text = re.sub('\n(\w)', ' \g<1>', formatted_text)
    formatted_text = re.sub(r" +", ' ', formatted_text)
    # more clean
    formatted_text = formatted_text.replace('“', '"')
    formatted_text = formatted_text.replace('”', '"')
    # formatted_text = formatted_text.replace('/', ' ')
    # formatted_text = formatted_text.replace('-', ' ')
    # formatted_text = formatted_text.replace(',', '')
    # formatted_text = formatted_text.replace(r'nº', r' número')
    # formatted_text = formatted_text.replace(r'nª', r'número')
    # formatted_text = formatted_text.replace(r' n ', r' número   ')
    # formatted_text = formatted_text.replace(r'(?<=n)[º\s+](?=\d)', r'_')
    # formatted_text = formatted_text.replace(r'(?<=n)[ª\s+](?=\d)', r'_')
    formatted_text = re.sub(r'rel. ', r'relator ', formatted_text, flags=re.I)
    formatted_text = re.sub(r'min. ', r'Ministro ', formatted_text, flags=re.I)
    formatted_text = re.sub(r'des. ', r'Desembargador ', formatted_text, flags=re.I)
    formatted_text = formatted_text.replace(r'fls. ', r'folhas_')
    formatted_text = formatted_text.replace(r'súmula n ', r'súmula_')
    formatted_text = formatted_text.replace(r'súmula ', r'súmula_')
    formatted_text = formatted_text.replace(r'súmulas ', r'súmulas_')
    formatted_text = formatted_text.replace(r'lei ', r'lei_')
    formatted_text = formatted_text.replace(r'art ', r'artigo_')
    formatted_text = formatted_text.replace(r'arts ', r'artigos_')
    formatted_text = formatted_text.replace(r'artigo ', r'artigo_')
    formatted_text = formatted_text.replace(r'inc ', r'inciso_')
    formatted_text = formatted_text.replace(r'inciso ', r'inciso_')
    formatted_text = formatted_text.replace(r'§ ', r'parágrafo_')
    formatted_text = formatted_text.replace(r'alínea ', 'alínea_')
    formatted_text = formatted_text.replace(r'paragrafo ', r'paragrafo_')
    formatted_text = formatted_text.replace(r'ministério público', r'ministério_público')
    formatted_text = formatted_text.replace(r'ministerio público', r'ministério_público')
    formatted_text = formatted_text.replace(r'código processo civil', r'código_processo_civil')
    formatted_text = formatted_text.replace(r'cpd ', r'código_processo_civil ')
    formatted_text = formatted_text.replace(r'código de defesa do consumidor', r'código_defesa_consumidor')
    formatted_text = formatted_text.replace(r'cdc ', r'código_defesa_consumidor ')
    # formatted_text = formatted_text.replace(r'dje ', r'diário_da_justiça_eletrônico ')
    formatted_text = formatted_text.replace(r' lc ', r' lei_complementar')
    formatted_text = formatted_text.replace(r'processo ', r'processo_')
    formatted_text = formatted_text.replace(r'erga omnes', r'erga_omnes')
    formatted_text = formatted_text.replace(r'ação civil publica', r'ação_civil_publica')
    formatted_text = formatted_text.replace(r'superiorribunal de justiça', r'stj')
    formatted_text = formatted_text.replace(r'supremo tribunal federal', r'stf')
    formatted_text = formatted_text.replace(r'(?=sú tmula_)(sumula_\d{1,5})\s+stj',
                                            r'\g<1>_stj')
    formatted_text = formatted_text.replace(r'(?=súmula_)(sumula_\d{1,5})\s+stf',
                                            r'\g<1>_stf')
    formatted_text = formatted_text.replace(r'(?=art_)(art_\d{1,5}).+(codigo) ([\w ]+)', r'\g<1>_\g<2>_\g<3>')

    return formatted_text

def main():
    st.header(":bookmark_tabs: Entidades Nomeadas")

    nlp = get_spacy_model()

    with st.sidebar:
        selected_files = st.multiselect(
                                    "Selecionar arquivo",
                                    options=st.session_state['all-files'],
                                    format_func=lambda f : f.replace('.txt', '')
                                )


    if len(selected_files) >= 1:
        selected = selected_files[0]
        
        
        text = get_document_content(selected)
        text = preprocessing(text)
        doc = nlp(text)
        ui_show_text_named_entities(selected, doc)

        entities = [{'label' : ent.label_,
                     'Entidades' : ent.text } for ent in doc.ents]

        df_entities = pd.DataFrame.from_records(entities)

        

        # st.dataframe(df_ents)
        with st.sidebar:
            ui_show_entity_table(df_entities)
            st.download_button("Baixar Acórdão",data=text, file_name=f"{selected}.txt")
    else :
        st.info("Selecione um registro para visualizar as entidades mencionadas.")
        

if __name__ == "__main__":
    main()
