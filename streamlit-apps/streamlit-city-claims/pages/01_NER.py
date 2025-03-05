import pandas as pd
import streamlit as st
import spacy
import sqlite3
from spacy_streamlit import visualize_ner

models = ["model"]
default_text = """Solicita à Secretaria Municipal de Serviços e Obras Públicas para que realize a manutenção do recape asfáltico na Rua Willian Villas Boas, e proceda a pavimentação asfáltica na Rua Dirceu Galvão, ambas as vias no Jardim Santa Terezinha. Reiterando pedido já realizado por meio do Requerimento nº 528/2020."""
# visualizers = ["ner"]# ["ner", "textcat"]
# spacy_streamlit.visualize(models, default_text, visualizers)

@st.cache_resource
def db_connection():
    return sqlite3.connect("requerimentos.db")

@st.cache_resource
def load_model():
    return spacy.load("model")

@st.cache_data
def load_data():
    con = db_connection()
    # df = pd.read_csv('requerimentos-ruas-3.csv')
    df = pd.read_sql("SELECT * FROM requerimento", con)
    return df

nlp = load_model()

def ui_show_ner(row):
    text = row.loc[row.index[0], 'ementa']
    doc = nlp(text)
    visualize_ner(doc, 
                  labels=nlp.get_pipe("ner").labels, 
                  show_table=False, 
                  title='Entidades Nomeadas')

def main():
    df = load_data()
    anos_disponiveis = ['2021', '2022', '2023']

    
    with st.form(key='pesquisa-requerimento'):
        col1, col2 = st.columns([2, 2])
        with col1:
            nro_req = st.text_input("Número:")
        with col2:
            ano_req = st.text_input("Ano: ")
        subimit = st.form_submit_button('Pesquisar')

    if subimit:
        nro_req = int(nro_req) if nro_req.isdigit() else 'ND'
        ano_req = int(ano_req) if (ano_req in anos_disponiveis) else 'ND'
        # st.write([nro_req, ano_req])
        row = df.loc[lambda d: (d.numero == nro_req) & (d.ano == ano_req)]
        if len(row) == 1:
            ui_show_ner(row)
            
              
    
    # st.warning("O requerimento procurado ainda não se encontra nas nossas bases de dados! Por favor, selecione outro.")

if __name__ == "__main__":
    main()