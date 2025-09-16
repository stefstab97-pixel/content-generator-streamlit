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
   Contenuto: "Scopri il tuo momento di relax con la nuova bevanda della stagione. #StarbucksMoments"
"""

# -----------------------------
# Sidebar: impostazioni principali
# -----------------------------
st.sidebar.title("⚙️ Parametri Generali")
company_name = st.sidebar.text_input("Nome Azienda", "GreenTech Solutions")
industry = st.sidebar.text_input("Settore", "Energie rinnovabili")
tone = st.sidebar.selectbox("Tono della comunicazione", ["Professionale", "Amichevole", "Motivazionale", "Ispirazionale"])
social_channel = st.sidebar.selectbox("Canale Social", ["LinkedIn", "Facebook", "Instagram", "Twitter"])
target_audience = st.sidebar.text_input("Pubblico Target", "Manager e professionisti nel settore green")
length = st.sidebar.slider("Numero di paragrafi del contenuto", 1, 5, 3)

# -----------------------------
# Main area: topic e esempi personalizzati
# -----------------------------
st.title("💡 Generatore di Contenuti Aziendali Avanzato")
topic = st.text_input("Argomento principale", "Importanza della sostenibilità nelle imprese")

st.markdown("### 📝 Esempi di riferimento (opzionali)")
user_examples = st.text_area("Puoi aggiungere esempi personalizzati per affinare lo stile", default_examples, height=200)

# -----------------------------
# Prompt template
# -----------------------------
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "Sei un esperto content writer per aziende. Genera contenuti professionali, creativi e coerenti con il brand."),
    ("user", f"""
Crea un contenuto pubblicitario per l'azienda {{company_name}}, settore {{industry}}, con tono {{tone}}.
Il contenuto deve essere adatto al canale {{social_channel}} e rivolto a {{target_audience}}.
Argomento principale: {{topic}}.
Numero di paragrafi: {{length}}.

Usa questi esempi come riferimento di stile e tono:
{user_examples}
""")
])

# Catena
content_chain = prompt_template | chat_model

# -----------------------------
# Funzione di generazione contenuti
# -----------------------------
def generate_content(company_name, industry, tone, topic, social_channel, target_audience, length):
    result = content_chain.invoke({
        "company_name": company_name,
        "industry": industry,
        "tone": tone,
        "topic": topic,
        "social_channel": social_channel,
        "target_audience": target_audience,
        "length": length
    })
    return result.content

# -----------------------------
# Bottone per generare contenuto
# -----------------------------
if st.button("Genera Contenuto"):
    with st.spinner("Sto generando il contenuto..."):
        content = generate_content(company_name, industry, tone, topic, social_channel, target_audience, length)
        st.markdown("### 📄 Contenuto Generato")
        with st.expander("Visualizza il contenuto completo"):
            st.markdown(content)
        # Bottone per download
        st.download_button("💾 Scarica il contenuto", content, file_name=f"{company_name}_contenuto.txt")
