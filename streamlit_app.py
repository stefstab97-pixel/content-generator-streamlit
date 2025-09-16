import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from PIL import Image
import requests
from io import BytesIO

# -----------------------------
# Streamlit: Sfondo personalizzato e logo
# -----------------------------
st.markdown(
    """
    <style>
    body {
        background-color: #c6e9f9;
        color: #0D0E11;
        font-family: 'Inter', sans-serif;
    }
    .custom-logo {
        font-size: 48px;
        color: #0D0E11;
        text-align: center;
        margin-top: 20px;
        font-weight: 700;
        text-shadow: 0 0 3px #0D0E11, 0 0 5px #0D0E11;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Logo testuale
st.markdown('<div class="custom-logo">💰 Sassa La Sussurratrice dei grandi brand 💰</div>', unsafe_allow_html=True)

# Immagine dei soldi come logo/illustrazione
img_url = "https://images.crushpixel.com/desktop/2458088/euro-banknotes-background.jpg"  # URL diretto all'immagine
response = requests.get(img_url)
img = Image.open(BytesIO(response.content))
st.image(img, width=400)

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

# Catena
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
st.title("💡 Generatore di Contenuti Aziendali")

company_name = st.text_input("Nome Azienda", "GreenTech Solutions")
industry = st.text_input("Settore", "Energie rinnovabili")
tone = st.selectbox("Tono", ["Professionale e motivazionale", "Amichevole", "Ironico", "Serio"])
topic = st.text_input("Argomento principale", "Importanza della sostenibilità nelle imprese")
social_channel = st.selectbox("Canale Social", ["LinkedIn", "Facebook", "Instagram", "Twitter"])
target_audience = st.text_input("Pubblico Target", "Manager e professionisti nel settore green")

if st.button("Genera Contenuto"):
    with st.spinner("Sto generando il contenuto..."):
        content = generate_content(company_name, industry, tone, topic, social_channel, target_audience)
        st.markdown("### 📄 Contenuto Generato")
        st.markdown(content)
