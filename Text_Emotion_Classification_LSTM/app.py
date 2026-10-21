# Text Emotion Classification Streamlit App
# This app loads the trained model and predicts the emotion in a sentence.

import json
import html
import os

import numpy as np
import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import tokenizer_from_json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "emotion_lstm.keras")
TOKENIZER_PATH = os.path.join(BASE_DIR, "tokenizer.json")
LABELS_PATH = os.path.join(BASE_DIR, "labels.json")
MAX_LEN = 40

st.set_page_config(
    page_title="Feeling, Found | Emotion Classifier",
    page_icon="✳",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Fraunces:opsz,wght@9..144,500;9..144,600&display=swap');

    :root {
        --ink: #202c28;
        --muted: #6b7771;
        --paper: #f7f7f2;
        --line: #dfe5dc;
        --green: #285b47;
        --green-light: #e6efe8;
        --coral: #d46e54;
        --gold: #d6a444;
        --blue: #668da0;
    }

    html, body, [class*="css"] {
        font-family: 'DM Sans', 'Segoe UI', sans-serif;
        color: var(--ink);
    }
    [data-testid="stAppViewContainer"] {
        background-color: var(--paper);
        background-image: linear-gradient(rgba(40, 91, 71, .035) 1px, transparent 1px),
                          linear-gradient(90deg, rgba(40, 91, 71, .035) 1px, transparent 1px);
        background-size: 32px 32px;
    }
    [data-testid="stHeader"] { background: transparent; }
    [data-testid="stMain"] > div { padding-top: 2.2rem; }
    .block-container { max-width: 1120px; padding-bottom: 3rem; }
    h1, h2, h3 { color: var(--ink); }
    h1, .display-title {
        font-family: 'Fraunces', Georgia, serif !important;
        font-weight: 500 !important;
        letter-spacing: 0 !important;
    }
    .eyebrow {
        color: var(--green);
        font-size: .76rem;
        font-weight: 700;
        letter-spacing: .12em;
        text-transform: uppercase;
        margin-bottom: .55rem;
    }
    h1.hero-title {
        font-family: 'Fraunces', Georgia, serif;
        font-size: clamp(2.5rem, 5vw, 4.2rem);
        line-height: 1.02;
        color: #143a2e !important;
        opacity: 1 !important;
        margin: 0;
    }
    .hero-copy { color: var(--muted); font-size: 1.04rem; margin-top: .85rem; }
    .rule { border-top: 1px solid var(--line); margin: 1.7rem 0 1.5rem; }
    .section-kicker {
        color: var(--muted);
        font-size: .76rem;
        font-weight: 700;
        letter-spacing: .1em;
        text-transform: uppercase;
        margin: .2rem 0 .8rem;
    }
    .emotion-strip {
        display: flex;
        gap: .55rem;
        flex-wrap: wrap;
        margin: .35rem 0 1.1rem;
    }
    .emotion-tag {
        border: 1px solid var(--line);
        background: rgba(255,255,255,.65);
        padding: .38rem .7rem;
        border-radius: 3px;
        font-size: .86rem;
        color: var(--ink);
    }
    .emotion-tag span { margin-right: .35rem; }
    [data-testid="stTextArea"] textarea {
        background: rgba(255,255,255,.82);
        border: 1px solid #cbd7cc;
        border-radius: 4px;
        min-height: 160px;
        color: var(--ink);
        font-size: 1rem;
        line-height: 1.6;
        padding: 1rem;
    }
    [data-testid="stTextArea"] textarea:focus {
        border-color: var(--green);
        box-shadow: 0 0 0 2px rgba(40,91,71,.12);
    }
    [data-testid="stTextArea"] label { display: none; }
    .stButton > button {
        border-radius: 3px;
        font-weight: 600;
        transition: transform .15s ease, background .15s ease;
    }
    .stButton > button:hover { transform: translateY(-1px); }
    [data-testid="stBaseButton-primary"] {
        background: var(--green);
        border-color: var(--green);
        min-height: 3rem;
    }
    .sample-caption { color: var(--muted); font-size: .86rem; margin: .3rem 0 .6rem; }
    .result-panel {
        background: #fff;
        border: 1px solid var(--line);
        border-top: 4px solid var(--green);
        border-radius: 4px;
        padding: 1.35rem 1.45rem;
        margin-top: .15rem;
        box-shadow: 0 8px 24px rgba(32,44,40,.045);
    }
    .result-label {
        color: var(--muted);
        font-size: .74rem;
        font-weight: 700;
        letter-spacing: .1em;
        text-transform: uppercase;
    }
    .result-emotion {
        font-family: 'Fraunces', Georgia, serif;
        font-size: 2.5rem;
        line-height: 1.05;
        margin: .45rem 0 .65rem;
        color: var(--green);
    }
    .result-quote {
        color: var(--muted);
        font-size: .94rem;
        line-height: 1.55;
        border-left: 2px solid var(--gold);
        padding-left: .8rem;
        margin: .8rem 0 1rem;
        overflow-wrap: anywhere;
    }
    .confidence-line {
        display: flex;
        justify-content: space-between;
        gap: 1rem;
        color: var(--ink);
        font-size: .9rem;
        font-weight: 600;
    }
    .probability-title { margin: 1.4rem 0 .7rem; font-weight: 700; font-size: .9rem; }
    .empty-panel {
        min-height: 318px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 1.7rem;
        border: 1px dashed #bdcbbf;
        border-radius: 4px;
        background: rgba(255,255,255,.38);
    }
    .empty-mark { color: var(--coral); font-size: 2rem; line-height: 1; }
    .empty-title {
        font-family: 'Fraunces', Georgia, serif;
        font-size: 1.65rem;
        color: #143a2e !important;
        margin: .8rem 0 .4rem;
    }
    .empty-copy { color: #485b51 !important; line-height: 1.6; }
    .stProgress > div > div > div > div { background: var(--green); }
    .footer-note {
        color: var(--muted);
        font-size: .78rem;
        border-top: 1px solid var(--line);
        margin-top: 2.2rem;
        padding-top: .9rem;
    }
    @media (max-width: 700px) {
        [data-testid="stMain"] > div { padding-top: 1.2rem; }
        .hero-title { font-size: 2.7rem; }
        .result-panel { padding: 1.1rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("The model is missing. Please run train_model.py first.")
    return tf.keras.models.load_model(MODEL_PATH)


@st.cache_resource
def load_labels():
    with open(LABELS_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data["labels"]


@st.cache_resource
def load_tokenizer():
    with open(TOKENIZER_PATH, "r", encoding="utf-8") as file:
        return tokenizer_from_json(file.read())


try:
    model = load_model()
    labels = load_labels()
    tokenizer = load_tokenizer()
except Exception as e:
    st.error("The model files could not be loaded.")
    st.caption("Run `python train_model.py` from this project folder, then refresh this page.")
    st.stop()


st.markdown(
    '<div class="eyebrow">A small study in language & feeling</div>'
    '<h1 class="hero-title">Feeling,<br>found.</h1>'
    '<div class="hero-copy">A sentence can carry more than one meaning. See which emotion comes through strongest.</div>'
    '<div class="rule"></div>',
    unsafe_allow_html=True,
)

emotion_details = {
    "joy": ("☀", "Joy"),
    "sadness": ("◒", "Sadness"),
    "anger": ("✳", "Anger"),
    "fear": ("△", "Fear"),
}
emotion_colors = {
    "joy": "#a06a13",
    "sadness": "#527b91",
    "anger": "#c15f49",
    "fear": "#6c6b91",
}


def set_sample_text(text):
    st.session_state.emotion_text = text


input_column, result_column = st.columns([1.08, 0.92], gap="large")

with input_column:
    st.markdown('<div class="section-kicker">01 / Choose your words</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="emotion-strip">'
        '<div class="emotion-tag"><span>☀</span>Joy</div>'
        '<div class="emotion-tag"><span>◒</span>Sadness</div>'
        '<div class="emotion-tag"><span>✳</span>Anger</div>'
        '<div class="emotion-tag"><span>△</span>Fear</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    if "emotion_text" not in st.session_state:
        st.session_state.emotion_text = ""

    user_text = st.text_area(
        "Sentence",
        key="emotion_text",
        placeholder="Write what's on your mind...",
        height=160,
        max_chars=500,
    )
    st.markdown('<div class="sample-caption">Need a starting point? Try a sample:</div>', unsafe_allow_html=True)

    sample_columns = st.columns(4, gap="small")
    samples = [
        ("Joy", "I feel happy and excited about today."),
        ("Sadness", "I miss the people I used to see every day."),
        ("Anger", "It is unfair that nobody listened to me."),
        ("Fear", "I feel nervous about what might happen next."),
    ]
    for sample_column, (sample_name, sample_text) in zip(sample_columns, samples):
        with sample_column:
            st.button(
                sample_name,
                key=f"sample_{sample_name.lower()}",
                use_container_width=True,
                on_click=set_sample_text,
                args=(sample_text,),
            )

    predict_clicked = st.button("Read the emotion  →", type="primary", use_container_width=True)
    if predict_clicked:
        if not user_text.strip():
            st.warning("Write a sentence first, or choose one of the samples above.")
        else:
            sequence = tokenizer.texts_to_sequences([user_text.strip()])
            padded = pad_sequences(sequence, maxlen=MAX_LEN, padding="post")
            st.session_state.emotion_prediction = model.predict(padded, verbose=0)[0].tolist()
            st.session_state.emotion_original_text = user_text.strip()

with result_column:
    st.markdown('<div class="section-kicker">02 / What comes through</div>', unsafe_allow_html=True)
    prediction = st.session_state.get("emotion_prediction")

    if prediction is None:
        st.markdown(
            '<div class="empty-panel">'
            '<div class="empty-mark">✳</div>'
            '<div class="empty-title">Your reading will appear here.</div>'
            '<div class="empty-copy">Write a sentence, then ask the model to read its strongest emotional signal.</div>'
            '</div>',
            unsafe_allow_html=True,
        )
    else:
        predicted_index = int(np.argmax(prediction))
        predicted_label = labels[predicted_index]
        confidence = float(prediction[predicted_index])
        icon, display_label = emotion_details.get(predicted_label, ("•", predicted_label.title()))
        safe_quote = html.escape(st.session_state.get("emotion_original_text", ""))

        st.markdown(
            f'<div class="result-panel" style="border-top-color:{emotion_colors.get(predicted_label, "#285b47")}">'
            f'<div class="result-label">Strongest signal</div>'
            f'<div class="result-emotion" style="color:{emotion_colors.get(predicted_label, "#285b47")}">{icon} {display_label}</div>'
            f'<div class="result-quote">“{safe_quote}”</div>'
            f'<div class="confidence-line"><span>Model confidence</span><span>{confidence:.1%}</span></div>'
            '</div>',
            unsafe_allow_html=True,
        )
        st.markdown('<div class="probability-title">All emotion signals</div>', unsafe_allow_html=True)
        for label_index, emotion in enumerate(labels):
            emotion_icon, emotion_name = emotion_details.get(emotion, ("•", emotion.title()))
            score = float(prediction[label_index])
            st.markdown(
                f'<div class="confidence-line"><span>{emotion_icon} {emotion_name}</span><span>{score:.1%}</span></div>',
                unsafe_allow_html=True,
            )
            st.progress(score, text=None)

st.markdown(
    '<div class="footer-note">Text Emotion Classification · Word Embedding + LSTM · Joy / Sadness / Anger / Fear</div>',
    unsafe_allow_html=True,
)
