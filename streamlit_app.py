import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# -----------------------------
# Streamlit: sfondo e neon-logo
# -----------------------------
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #0D0E11 0%, #0D0E11 100%);
        color: white;
        font-family: 'Inter', sans-serif;
    }
    .neon-logo {
        font-size: 48px;
        color: #3AB4F2;
        text-align: center;
        margin-top: 50px;
        text-shadow: 0 0 5px #3AB4F2, 0 0 15px #3AB4F2, 0 0 30px #3AB4F2;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { text-shadow: 0 0 5px #3AB4F2, 0 0 15px #3AB4F2; }
        50% { text-shadow: 0 0 15px #3AB4F2, 0 0 25px #3AB4F2; }
        100% { text-shadow: 0 0 5px #3AB4F2, 0 0 15px #3AB4F2; }
    }
    .stButton>button {
        background-color: #3AB4F2;
        color: #0D0E11;
        font-weight: 600;
        border-radius: 10px;
        height: 45px;
        width: 100%;
        border: none;
        margin-top: 10px;
    }
    .stTextInput>div>div>input {
        background-color: #1A1B1F;
        color: white;
        border-radius: 8px;
        height: 35px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="neon-logo">🤖 Bot Aziendale</div>', unsafe_allow_html=True)
st.title("💡 Generatore di Contenuti Aziendali")

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
# Streamlit UI: input
# -----------------------------
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
