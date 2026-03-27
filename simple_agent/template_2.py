"""
Simple Agent - Template 2: FAQ Bot
Arquitectura: Single-Agent
Sin API Key requerida
"""

import streamlit as st
import random

st.set_page_config(page_title="Simple Agent T2", page_icon="🤖")

st.title("🤖 Simple Agent - Template 2")
st.markdown("**Arquitectura:** Single-Agent | **Modo:** FAQ Bot")

st.markdown("---")

faq_database = {
    "que es python": "Python es un lenguaje de programacion de alto nivel, interpretado y orientado a objetos.",
    "que es javascript": "JavaScript es un lenguaje de programacion para desarrollo web que permite crear interactividad.",
    "que es html": "HTML (HyperText Markup Language) es el lenguaje de marcado estandar para crear paginas web.",
    "que es css": "CSS (Cascading Style Sheets) es un lenguaje para describir la presentacion de documentos HTML.",
    "que es api": "API (Application Programming Interface) es un conjunto de protocolos para comunicar aplicaciones.",
    "que es machine learning": "Machine Learning es una rama de la inteligencia artificial que permite a las maquinas aprender.",
    "que es deep learning": "Deep Learning es un subcampo del machine learning basado en redes neuronales profundas.",
    "que es git": "Git es un sistema de control de versiones distribuido para rastrear cambios en codigo.",
    "que es docker": "Docker es una plataforma para desarrollar, enviar y ejecutar aplicaciones en contenedores.",
    "que es cloud": "Cloud Computing es la entrega de servicios de computacion a traves de internet.",
}


def get_faq_response(user_input):
    user_lower = user_input.lower().strip()

    for question, answer in faq_database.items():
        if question in user_lower or user_lower in question:
            return answer

    return random.choice(
        [
            "Esa pregunta no esta en mi base de conocimientos. Intenta con una pregunta sobre programacion o tecnologia.",
            "No tengo informacion sobre eso. Puedo responder preguntas sobre Python, JavaScript, HTML, CSS, API, Machine Learning, Git, Docker y Cloud.",
            "Pregunta no reconocida. Prueba preguntando sobre alguno de estos temas: programacion web, lenguajes, herramientas de desarrollo.",
        ]
    )


if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown("### 💬 FAQ Bot")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Haz una pregunta sobre programacion o tecnologia...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = get_faq_response(prompt)
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

st.markdown("---")
st.markdown("### Temas Disponibles")
cols = st.columns(2)
topics = list(faq_database.keys())
for i, topic in enumerate(topics):
    with cols[i % 2]:
        st.markdown(f"- {topic.replace('que es ', '').title()}")

st.markdown("""
### Acerca de este Template

**Template 2: FAQ Bot**

Base de conocimientos integrada con respuestas predefinidas.
Funciona completamente sin API key.
""")
