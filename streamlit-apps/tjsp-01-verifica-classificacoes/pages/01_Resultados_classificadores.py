import streamlit as st
import pandas as pd
import numpy as np
import re

from datetime import datetime, timedelta
from pathlib import Path
from time import time
from streamlit.components.v1 import html
from streamlit.runtime.scriptrunner import get_script_run_ctx

from pandas.api.types import (
    is_categorical_dtype, 
    is_numeric_dtype
)

@st.cache_data(ttl=None)
def get_user_folder(user_id):

    base_folder = Path('data', 'visitors')
    if not base_folder.exists() :
        base_folder.mkdir(parents=True)
    # python doesn't have a do... while loop
    while True:
        user_folder = base_folder / datetime.now().strftime("%Y-%m-%dT%H-%M-%S-%f")
        if not user_folder.exists():
            break
    ctx = get_script_run_ctx()
    print(ctx.session_id)
    
    return user_folder

st.set_page_config(
                page_title="Avaliação",
                layout='wide', 
                initial_sidebar_state="expanded"
                )

# CONFIGURAÇÕES SESSION STATE
if 'dataframe' not in st.session_state:
    st.session_state.dataframe = None

if 'result_folder' not in st.session_state:
    st.session_state.result_folder = Path('data', 'results')
    if not st.session_state.result_folder.exists():
        st.session_state.result_folder.mkdir()

if not 'user_folder' in st.session_state:
    if not Path('data', 'visitors').exists():
        Path('data', 'visitors').mkdir()
    ctx = get_script_run_ctx()
    st.session_state.user_folder = get_user_folder(ctx.session_id)

if not 'previous_comments' in st.session_state:
    st.session_state.previous_comments = list()

def reset_dataframe():
    st.session_state.dataframe = None

# UI LOAD DATASET AND FILTER IT
def rename_column_function(column):
        if '_' in column :
            column = column.replace('_', ' ')
        if re.search(r'\d{3,}', column) :
            column = re.sub(r'[ a-zA-Z.]{0,}(\d+)', r"Probabilidade \1", column)
        column = column.capitalize()
        return column

@st.cache_data()
def load_dataset(filelike):
    print("Executando... ")
    df = pd.read_csv(filelike, dtype = {
                'numero_processo' : 'string',
                'id_documento' :'string',
                'natureza_processo' :'string',
                'codigos_movimentos_temas' : 'string',
                'temas' : 'category',
                'predição' : 'category',
                'Proba. tema 0929' :'float', # probabilidade_0929
                'Proba. tema 1015' :'float',
                'Proba. tema 1033' :'float',
                'Proba. tema 1039' :'float',
                'Proba. tema 1101' :'float',
            })
        
    return df

def ui_load_dataset():
    uploaded_file = st.file_uploader("Subir arquivo:") # on_change=reset_dataframe
    
    if st.button("Analisar") and (uploaded_file is not None):
        
        with st.spinner():
            df = load_dataset(uploaded_file)
            # df.rename(columns=rename_column_function, inplace=True)
            
        st.session_state.dataframe = df
    else :
        df = st.session_state.dataframe

    return df

def ui_filtering(df):
    tab1, tab2, tab3 = st.tabs(["Básico", "Filtros", "Ver colunas"])

    with tab1 :
        df = ui_predefine_filters(df)

    with tab2:
        df = ui_filtering_dataset(df)

    with tab3 :
        df = ui_select_columns(df)

    return df

def recalc_predictions(df : pd.DataFrame):
    threshold = st.slider("Selecione um threshold", min_value=50, max_value=100)
    predictions = df.filter(regex="probabilidade_{0,1}\d{3,4}")

    labels = [re.findall('\d+', str(c)) for c in df.columns if c.lower().startswith('probabilidade')]
    labels = [int(l[0]) for l in labels if len(l) == 1]
    
    df['predição'] = (predictions > threshold).apply(lambda x : tuple(labels[i] for i, v in enumerate(x) if v), axis=1)

    return df

def ui_predefine_filters(df):

    options = [
        (0, 'Ver todos os registros'),
        (70, 'Selecionar threshold')
    ]

    code, _ = st.selectbox("Selecionar critério",
                options=options,
                format_func=lambda x : x[1])
    
    if code == 70 :
        df = recalc_predictions(df)

    return df

def ui_filtering_dataset(dataframe):
    def is_default(col):
        return (col.lower().startswith('tema')) 
    
    columns = list(dataframe.columns)
    defaults = filter(is_default, columns)
        
    dataframe = dataframe.copy()

    modification_container = st.container()

    with modification_container:
        to_filter_columns = st.multiselect("Filtrar por colunas:", columns, defaults)
        for column in to_filter_columns:
            left, right = st.columns((1, 20))
            left.write("↳")
            # Treat columns with < 10 unique values as categorical
            if is_categorical_dtype(dataframe[column]) or dataframe[column].nunique() < 10:
                user_cat_input = right.multiselect(
                    f"Selecione valores para {column}",
                    dataframe[column].unique(),
                    default=list(dataframe[column].unique()),
                )
                dataframe = dataframe[dataframe[column].isin(user_cat_input)]

            elif is_numeric_dtype(dataframe[column]):
                _min = float(dataframe[column].min())
                _max = float(dataframe[column].max())
                step = (_max - _min) / 100
                user_num_input = right.slider(
                    f"Selecione o intervalo {column}",
                    _min,
                    _max,
                    (_min, _max),
                    step=step,
                )
                dataframe = dataframe[dataframe[column].between(*user_num_input)]

            else:
                user_text_input = right.text_input(
                    f"Substring ou regex em {column}",
                )
                if user_text_input:
                    dataframe = dataframe[dataframe[column].str.contains(user_text_input)]

    # df = dataframe[selected_columns]

    return dataframe

def ui_select_columns(df):
    def is_default(col):
        return ('processo' in col.lower()) \
            or ('probabilidade' in col.lower()) \
            or ('conteudo' in col.lower()) \
            or ('predição' in col.lower()) \
            or (col.lower().startswith('tema'))
    
    # como a lista é representada: (indice, nome da coluna)
    options = list(df.columns)
    defaults = filter(is_default, options)
    selected_columns = st.multiselect(
                            "Escolha quais as colunas deseja visualizar.",
                            options, defaults
                        )
    
    return df[selected_columns]
    # return df

def ui_show_dataframe(df, gradient=False):
    columns = [ c for c in df.columns if c.lower() != 'conteudo']
    df = df[columns]
    gradient = st.checkbox("Colorir colunas das probabilidades")
    st.write(f"*{df.shape[0]} registros selecionados*")
    if gradient:
        proba_columns = [c for c in df.columns if c.lower().startswith('proba')]
        try:
            st.dataframe(
                    df.style.background_gradient(subset=proba_columns).format(precision=2), 
                    use_container_width=True, 
                    height=500
                )
        except KeyError :
            st.dataframe(
                    df, 
                    use_container_width=True, 
                    height=500
                )
            st.warning("Não foi possível definir o gradiente. Provavelmente o tamanho do dataset exibido dificulta a operação")
    else:
        st.dataframe(
                df, 
                use_container_width=True, 
                height=500
            )

## - - - - - - - - - - - - - - - - - - - -
# UI USER INTERACTION
def display_document_text(document, label_for_content):
    '''
    See more available colors:
    <https://www.w3schools.com/cssref/css_colors.php>
    '''
    content = document.iloc[0][label_for_content]
    html(f"<pre style='background-color : #F8F8FF'>{content}</pre>", height=700, scrolling=True)

def display_attrs(document, attr):
    st.table(document[attr].T)

def ui_user_interaction(dataframe):
    
    columns_relative_space = [10, 4]

    all_columns = list(dataframe.columns)
    label_id_document = 'Numero processo' if ('Numero processo' in dataframe.columns) else 'numero_processo'
    label_for_content  = 'Conteudo' if ('Conteudo' in dataframe.columns) else 'conteudo'
    id_document = None
    st.subheader("Visualizar conteúdo do acórdão")

    if label_for_content not in dataframe.columns:
        text = "Não foi possível identificar uma coluna para o texto dos acórdãos no dataset informado"
        st.warning(text)
        return None
    
    if label_id_document not in dataframe.columns:
        text = "Não foi possível identificar a coluna com o número de processo no dataset informado.\nCampo esperado: Numero processo"

    # display_select_document, display_simple_header = st.columns(columns_relative_space)

    selected_values = st.multiselect("Número do processo:", dataframe[label_id_document].unique())    
    id_document = selected_values[0] if len(selected_values) >=1 else None           

    if id_document is not None:
        document = dataframe.loc[lambda df: df[label_id_document] == id_document]
        col_display_content, col_display_others_attrs = st.columns(columns_relative_space)
    
        with col_display_content :
            display_document_text(document, label_for_content)

        with col_display_others_attrs :
            st.write("**Detalhes do processo:**")
            attrs = [c for c in all_columns 
                        if c.lower().startswith('proba') \
                            or c.lower().startswith('tema') \
                            or c.startswith('prediç')
                    ]
            attrs.insert(0, label_id_document)
            display_attrs(document, attrs)
            with st.form('form-suggestion', clear_on_submit=True):
                suggestion = st.multiselect(
                    "Sugerir novo tema ao processo:",
                    ['0929', '1015', '1033', '1039', '1101'],
                    )
                remark = st.text_area("Observação", height=170)
                submit = st.form_submit_button("Comentário")
        if submit :
            comment = {
                    'date' : datetime.now(),
                    'username' : 'Usuário não identificado', #username,
                    'text' : remark,
                    'id_processo' : id_document,
                    'tema_sugerido' : ', '.join(suggestion),
                    'saved' : False
                }
            st.session_state.previous_comments.append(comment)
    else: 
        st.info("Selecione um processo para visualizar o seu conteúdo")

    if st.session_state.previous_comments:
        ui_show_previous_comments(st.session_state.previous_comments)
        ui_save_comments(st.session_state.previous_comments, st.session_state.user_folder)

    return dataframe

## - - - - - - - - - - - - - - - - - - - -
## UI COMMENTS
def ui_comment_input_form(username='Usuário não identificado', nro_processo='...'):
    
    with st.form(key='form_comments', clear_on_submit=True) :
        col1, col2 = st.columns(2)
        username = col1.text_input("Nome: ", value=username)
        _ = col2.date_input("Data:", disabled=True, help="Identifica quando o comentário foi feito.")
        id_processo = st.text_input("Número do processo: (caso seja necessário) ", 
                                    value=nro_processo,
                                    help="Digite o número de um processo para fazer um comentário específico sobre um registro."
                                )
        
        text = st.text_area('Seu comentário:', placeholder='Escreva aqui...')
        
        col3, col4 = st.columns([1, 10])
        submitted = col3.form_submit_button("Comentar", type='primary')
        col4.form_submit_button("Limpar", type='secondary')

    if submitted:
        comment = {
            'date' : datetime.now(),
            'username' : username,
            'text' : text,
            'id_processo' : id_processo,
            'saved' : False
        }

        if len(text) < 5:
            placeholder = st.empty()
            with st.spinner():
                placeholder.warning("O texto do comentário não é válido. Por favor, verifique")
                time.sleep(2)
            placeholder.empty()
        else: 
            ui_take_comment(comment)

def ui_take_comment(comment):
    st.session_state.previous_comments.append(comment)

def ui_show_previous_comments(previous_comments):
    if len(previous_comments) < 1 :
        # sem comentários para mostrar
        return None 
    
    COMMENT_TEMPLATE = """
<div style="margin-top: 15px; margin-bottom: 15px; padding: 8px; border-radius: 10px; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);">
  <p><strong>{}</strong> escreveu em: <strong>{}</strong></p>
  <p style="color: #262626;">{}</p>
  <p style="color: #262626;">Processo: {}</p>
</div>
"""
    now = datetime.now()
    previous_comments = sorted(previous_comments, 
                               key=lambda c : c.get('date', now),
                               reverse=True
                               )
    placeholder = st.empty()
    with placeholder.container():
        st.header("Comentários")
        for c in previous_comments:
            st.markdown(
                COMMENT_TEMPLATE.format(
                    c.get('username', 'Usuário não identificado'),
                    c.get('date', now).strftime("%d/%m/%Y - %H:%M"), 
                    c.get('text'),
                    c.get('id_processo')),
                unsafe_allow_html=True,
            )

def ui_save_comments(previous_comments, destination=None, filename='comments.csv') :
    # check
    if (previous_comments is None or len(previous_comments) == 0) :
        return False
    # check

    if (len(previous_comments) >= 2):
        last = previous_comments[-1]
        second_last = previous_comments[-2]
        now = datetime.now()
        # delta = timedelta(minutes=3)
        delta = timedelta(seconds=30)
        if (last.get('date', now) - second_last.get('date', now + delta)) < delta:
            return False
    if not destination.exists():
        destination.mkdir(parents=True)

    destination = Path(destination) if (destination is not None) else Path('data', filename)
    destination = Path(destination, filename) if destination.is_dir() else destination

    tmp = pd.DataFrame.from_dict([c for c in previous_comments if not c['saved']])
    tmp.to_csv(destination, 
               index=False,
               header=(not destination.exists()),
               sep="|", 
               mode='a',
               quotechar="'")
    
    for comment in previous_comments:
        if not comment['saved'] :
            comment['saved'] = True

    return True

def main():
    st.header("Analisar Resultados")

    # Selecionar arquivos
    df = ui_load_dataset()

    if df is not None:

        with st.sidebar :
            df = ui_predefine_filters(df)
            df = ui_filtering_dataset(df)
            df = ui_select_columns(df)

    # Analisar Resultados
        st.subheader("Visualizar dados")
        
        ui_show_dataframe(df)
        # Visualizar individualmente um processo e comentários
        ui_user_interaction(df)

if __name__ == "__main__":
    # if logado:
    #     main(username, date.today())
    # else :
        # aparece a tela de login
    main()
