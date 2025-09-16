import streamlit as st
from PIL import Image
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# -----------------------------
# Inizializzazione modello
# -----------------------------
chat_model = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

# -----------------------------
# Few-shot examples
# -----------------------------
examples = """
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

Questi esempi aiutano a comprendere lo stile e il tono da generare.
"""

# -----------------------------
# Prompt template
# -----------------------------
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "Sei un esperto content writer per aziende. Genera contenuti professionali, creativi e coerenti con il brand."),
    ("user", f"""
Crea un contenuto pubblicitario per l'azienda {{company_name}}, settore {{industry}}, con tono {{tone}}.
Il contenuto deve essere adatto al canale {{social_channel}} e rivolto a {{target_audience}}.
Argomento principale: {{topic}}.

Usa questi esempi come riferimento di stile e tono:
{examples}
""")
])

# -----------------------------
# Catena
# -----------------------------
content_chain = prompt_template | chat_model

# -----------------------------
# Funzione di generazione contenuti
# -----------------------------
def generate_content(company_name, industry, tone, topic, social_channel, target_audience):
    result = content_chain.invoke({
        "company_name": company_name,
        "industry": industry,
        "tone": tone,
        "topic": topic,
        "social_channel": social_channel,
        "target_audience": target_audience
    })
    return result.content

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(
    page_title="💡 Generatore di Contenuti Aziendali",
    page_icon="💰",
    layout="wide"
)

# Sfondo colore turchese chiaro
st.markdown(
    """
    <style>
    .stApp {
        background-color: #c6e9f9;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💡 Generatore di Contenuti Aziendali")

# Logo con emoji 💰
st.markdown("### 💰 Sassa La Sussurratrice dei grandi brand")

# Immagine/logo locale
img = Image.open("euro-banknotes-background-2458088.jpg")
st.image(img, use_container_width=True)  # aggiornato secondo il nuovo parametro

# Input utente con menù a tendina
company_name = st.text_input("Nome Azienda", "GreenTech Solutions")
industry = st.selectbox("Settore", ["Energie rinnovabili", "Tecnologia", "Moda", "Caffetteria", "Finanza"])
tone = st.selectbox("Tono", ["Professionale", "Motivazionale", "Amichevole", "Innovativo"])
topic = st.text_input("Argomento principale", "Importanza della sostenibilità nelle imprese")
social_channel = st.selectbox("Canale Social", ["LinkedIn", "Instagram", "Facebook", "Twitter"])
target_audience = st.text_input("Pubblico Target", "Manager e professionisti nel settore green")

if st.button("Genera Contenuto"):
    with st.spinner("Sto generando il contenuto..."):
        content = generate_content(company_name, industry, tone, topic, social_channel, target_audience)
        st.markdown("### 📄 Contenuto Generato")
        st.markdown(content)
