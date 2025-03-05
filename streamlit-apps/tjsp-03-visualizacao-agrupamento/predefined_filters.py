import streamlit as st

from doubtlab.reason import ProbaReason
from doubtlab.reason import WrongPredictionReason
from doubtlab.reason import LongConfidenceReason
from doubtlab.reason import ShortConfidenceReason
from doubtlab.reason import MarginConfidenceReason
from doubtlab.reason import CleanlabReason

def when_probas_are_low_for_any_label(df, threshold=0.55):
    columns = [c for c in df.columns if c.startswith('Proba')]
    predicates = ProbaReason.from_proba(df[columns], max_proba=threshold)
    return df.loc[predicates != 0.0 ]

def when_model_makes_wrong_prediction(df):
    if ('1º tema sugerido' not in df.columns) \
        or ('temas' not in df.columns) :
        return df
    
    predictions = df['1º tema sugerido'].values
    y = df['temas'].values
    predicates =  WrongPredictionReason.from_predict(predictions, y)

    return df.loc[predicates != 0.0 ]

def when_wrong_label_gains_high_confidence(df, threshold=0.9):

    columns = [c for c in df.columns if c.startswith('Proba')]
    labels = [c.replace("Proba. tema", "").strip() for c in columns]
    y_test = df['temas'].values
    probas = df[columns].values

    predicates = LongConfidenceReason.from_proba(probas, y_test, labels, threshold=threshold)

    return df.loc[predicates != 0.0 ]

def when_correct_label_gains_low_confidence(df, threshold=0.3):
    columns = [c for c in df.columns if c.startswith('Proba')]
    labels = [c.replace("Proba. tema", "").strip() for c in columns]
    y_test = df['temas'].values
    probas = df[columns].values

    predicates = ShortConfidenceReason.from_proba(probas, y_test, labels, threshold=threshold)

    return df.loc[predicates != 0.0 ]

def when_there_is_small_diff_between_top_two_labels(df, threshold=0.2):
    
    columns = [c for c in df.columns if c.startswith('Proba')]
    probas = df[columns].values
    predicates = MarginConfidenceReason.from_proba(probas, threshold=threshold)

    return df.loc[predicates != 0.0 ]

@st.cache_data(ttl=1800, max_entries=5)
def when_confidence_learning(df):
    columns = [c for c in df.columns if c.startswith('Proba')]
    labels = [c.replace("Proba. tema", "").strip() for c in columns]
    probas = df[columns].values
    y_test_idx = df['temas'].apply(lambda x: labels.index(x))

    predicates = CleanlabReason.from_proba(probas, y_test_idx)
    
    return df.loc[predicates != 0.0]

# - - - - - - - - - -