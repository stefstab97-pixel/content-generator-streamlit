import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# -----------------------------
# Aggiungi CSS per lo sfondo
# -----------------------------
st.markdown(
    """
    <style>
    /* Sfondo gradiente */
    .stApp {
        background: linear-gradient(135deg, #6a11cb, #2575fc);
        color: white;
    }
    /* Titoli più grandi e leggibili */
    h1, h2, h3 {
        color: #ffffff;
    }
    /* Box per input con bordi arrotondati */
    .stTextInput>div>div>input {
        border-radius: 8px;
        padding: 8px;
    }
    /* Pulsanti più visibili */
    .stButton>button {
        background-color: #ff7f50;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Inizializzazione modello
# -----------------------------
chat_model = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

# -----------------------------
# Few-shot examples di default
# -----------------------------
default_examples = """
Esempi di contenuti generati per aziende famose:

1. Azienda: Nike
   Settore: Abbigliamento sportivo
   Tono: Motivazionale
   Canale: Instagram
   Pubblico: Giovani atleti
   Contenuto: "Sconfiggi i tuoi limiti. Indossa Nike e supera ogni traguardo. #JustDoIt"

2. Azienda: Starbucks
   Settore: Caffetteria
   Tono: Amichevole e caloroso
   Canale: Facebook
   Pubblico: Clienti fedeli
   Contenuto: "Scopri il tuo momento di relax con la nuova bevanda della stagione.
