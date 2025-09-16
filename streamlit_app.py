import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# -----------------------------
# CSS avanzato per sfondo e animazioni
# -----------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@600&display=swap');

    /* Sfondo nero con accenti neon-cyan e particelle */
    .stApp {
        background: #0D0E11;
        color: #FFFFFF;
        font-family: 'Inter', sans-serif;
        overflow: hidden;
        position: relative;
    }

    /* Neon glow per pulsazioni */
    .neon-logo {
        font-size: 64px;
        color: #3AB4F2;
        text-align: center;
        text-shadow:
            0 0 5px #3AB4F2,
            0 0 10px #3AB4F2,
            0 0 20px #3AB4F2,
            0 0 40px #3AB4F2;
        animation: pulse 2s infinite;
        margin-top: 50px;
    }

    @keyframes pulse {
        0% { text-shadow: 0 0 5px #3AB4F2, 0 0 10px #3AB4F2, 0 0 20px #3AB4F2, 0 0 40px #3AB4F2; }
        50% { text-shadow: 0 0 10px #3AB4F2, 0 0 20px #3AB4F2, 0 0 40px #3AB4F2, 0 0 60px #3AB4F2; }
        100% { text-shadow: 0 0 5px #3AB4F2, 0 0 10px #3AB4F2, 0 0 20px #3AB4F2, 0 0 40px #3AB4F2; }
    }

    /* Box input traslucido con glow */
    .stTextInput>div>div>input {
        border-radius: 10px;
        padding: 10px;
        background: rgba(58, 180, 242, 0.1);
        color: white;
        border: 1px solid #3AB4F2;
    }

    .stButton>button {
        background-color: #3AB4F2;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 12px 24px;
        transition: transform 0.2s;
    }

    .stButton>button:hover {
        transform: scale(1.05);
    }

    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Modello e prompt
# -----------------------------
chat_model = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

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

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "Sei un esperto content writer per aziende. Genera contenuti professionali, creativi e coerenti con il brand."),
    ("user", f"""
Crea un contenuto pubblicitario per l'azienda {{company_name}}, settore {{industry}}, con tono {{tone}}.
Il contenuto deve essere adatto al canale {{social_channel}} e rivolto a {{target_audience}}.
Argomento principale: {{topic}}.

Usa questi esempi come riferimento di stile e tono:
{default_examples}
""")
])

content_chain = prompt_template | chat_model

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
st.title("💡 Generatore di Contenuti Aziendali Avanzato")

# Logo neon-cyan pulsante
st.markdown('<div class="neon-logo">🤖 Bot Aziendale</div>', unsafe_allow_html=True)

company_name = st.text_input("Nome Azienda", "GreenTech Solutions")
industry = st.text_input("Settore", "Energie rinnovabili")
tone = st.text_input("Tono", "Professionale e motivazionale")
topic = st.text_input("Argomento principale", "Importanza della sostenibilità nelle imprese")
social_channel = st.text_input("Canale Social", "LinkedIn")
target_audience = st.text_input("Pubblico Target", "Manager e professionisti nel settore green")

if st.button("Genera Contenuto"):
    with st.spinner("Sto generando il contenuto..."):
        content = generate_content(company_name, industry, tone, topic, social_channel, target_audience)
        st.markdown("### 📄 Contenuto Generato")
        st.markdown(content)
