import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Inizializzazione modello
chat_model = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

# Prompt template
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "Sei un esperto content writer per aziende..."),
    ("user", """
Crea un contenuto pubblicitario per l'azienda {company_name}, settore {industry}, con tono {tone}.
Il contenuto deve essere adatto al canale: {social_channel} e rivolto a {target_audience}.
Argomento principale: {topic}.
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

# Streamlit UI
st.title("Generatore di Contenuti Aziendali")
company_name = st.text_input("Nome Azienda")
industry = st.text_input("Settore")
tone = st.text_input("Tono")
topic = st.text_input("Argomento")
social_channel = st.text_input("Canale Social")
target_audience = st.text_input("Pubblico Target")

if st.button("Genera Contenuto"):
    content = generate_content(company_name, industry, tone, topic, social_channel, target_audience)
    st.markdown(content)
