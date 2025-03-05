import streamlit as st
import altair as alt
import myOwnLib as my
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

def ui_sidebar_configuration():

    with st.sidebar:
        st.header("Parâmetros")
        algorithm = ''
        n_groups  = ''
        epsilon   = ''
        ns        = ''
        feature   = ''
        ngram     = ''
        vec_size  = ''
        df        = ''

        options = [' ', 'K-Means', 'K-Medoids', 'SOM', 'DBSCAN']
        algorithm = st.selectbox('Algoritmos', options)

        if algorithm in ['K-Means', 'K-Medoids', 'SOM']:
            n_groups     = st.slider("Número de agrupamentos:", 2, 20, 3)
        
        elif algorithm in ['DBSCAN']:
            epsilon = st.slider("EPS:", 1, 10, 3)
            epsilon = epsilon/10
            ns    = st.slider("Amostras:", 0, 40, 10)

        feature_type = [' ', 'Hash', 'Counting', 'TFIDF', 'Doc2Vec', 'Word2Vec']
        feature = st.selectbox('Feature', feature_type)

        if feature in ['Hash', 'Counting', 'TFIDF']:
            ngram_options = [1, 2, 3, 4, 5, 6]
            ngram   = st.multiselect("NGRAMS:", ngram_options)
            vec_size = st.slider("Dimensão do vetor:", 128, 2048, 1024)

        arquivo = st.file_uploader("Selecione um arquivo", type=["csv", "txt", "xlsx"])

        if arquivo is not None:
            # Verificar o tipo de arquivo enviado
            tipo_arquivo = arquivo.name.split('.')[-1]

            # Processar o arquivo enviado
            if tipo_arquivo == 'csv':
                df = pd.read_csv(arquivo)
            elif tipo_arquivo == 'txt':
                df = pd.read_table(arquivo)
            elif tipo_arquivo in ['xls', 'xlsx']:
                df = pd.read_excel(arquivo)
            else:
                st.error("Tipo de arquivo não suportado. Por favor, selecione um arquivo CSV, TXT ou Excel (XLS ou XLSX).")
    
    setup = dict(
            algorithm = algorithm,
            n_groups  = n_groups,
            epsilon   = epsilon,
            ns        = ns,
            feature   = feature,
            ngram     = ngram,
            vec_size  = vec_size,
            df        = df
        )

    return setup


def main():
    st.title(":crystal_ball: Análise de Agrupamentos")

    setup = ui_sidebar_configuration()


    if st.button("Processar"):
        df = setup['df']
        clusters, features = my.processCluster(df, 
                                             setup['algorithm'],
                                             setup['n_groups'],
                                             setup['feature'], 
                                             setup['vec_size'], 
                                             [min(setup['ngram']), max(setup['ngram'])])
        labels = [{'label' : str(i), 'idx' : idx} 
                    for i, cluster in enumerate(clusters)
                        for idx in cluster]
        labels = sorted(labels, key=lambda e: e['idx'])
        data = {
            'x1': features[:,0],
            'x2': features[:,1],
            'label' : [e['label'] for e in labels],
            'processo' : df['numero_processo'],
        }

        data = pd.DataFrame(data).assign(
            r=0
        )

        # st.dataframe(data, use_container_width=True)

        brush = alt.selection_interval()
        single = alt.selection_single(on='click', nearest=True)

        p1 = (alt.Chart(data)
                 .mark_circle(size=50) # opacity=0.5,
                 .encode(
                     x=alt.X('x1', axis=None, scale=alt.Scale(zero=False)),
                     y=alt.Y('x2', axis=None, scale=alt.Scale(zero=False)),
                     color=alt.condition(brush, 'label:N', alt.value('lightgray')),
                     tooltip=['processo']
                 )
                 .add_params(brush)
                 .properties(
                     width=750,
                     height=750,
                     title=f"Agrupamento {setup['algorithm']}"
                )
        )

        p2 = ( alt.Chart(data)
                  .mark_text(
                      align='right',
                      fontSize=15
                  )
                  .encode(
                      x=alt.X("r", axis=None),
                      y=alt.Y("row_number:O", axis=None),
                      text='processo:N'
                  )
                  .transform_window(row_number="row_number()")
                  .transform_filter(brush)
                  .transform_window(rank="rank(row_number)")
                  .transform_filter(alt.datum.rank < 15)
                  .properties(title="Número processo")
        )

        chart = (p1 | p2).configure_axis(grid=False).configure_view(strokeWidth=0)

        st.altair_chart(chart, use_container_width=False, theme="streamlit")

if __name__ == "__main__":
    main()