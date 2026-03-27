"""
Simple Agent - Template 1: Basic Assistant
Arquitectura: Single-Agent (Basico)
Sin API Key requerida - usa respuestas basadas en templates
"""

import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="Simple Agent T1", page_icon="🤖")

st.title("🤖 Simple Agent - Template 1")
st.markdown("**Arquitectura:** Single-Agent | **Modo:** Offline (sin API key)")

st.markdown("---")

templates_t1 = {
    "saludo": [
        "Hola! Soy tu asistente virtual. Como puedo ayudarte hoy?",
        "Bienvenido! Estoy aqui para asistirte. Que necesitas?",
    ],
    "ayuda": [
        "Puedo ayudarte con: informacion general, consejos, y mas.",
        "Mis capacidades incluyen responder preguntas y proporcionar informacion util.",
    ],
    "despedida": [
        "Fue un placer ayudarte! Vuelve pronto.",
        "Hasta luego! Estoy aqui cuando me necesites.",
    ],
    "default": [
        "Entiendo tu consulta. Para respuestas mas detalladas, configura una API key.",
        "Gracias por tu mensaje. Con una API key podre darte respuestas mas personalizadas.",
    ],
}


def get_response_t1(user_input):
    user_lower = user_input.lower()

    if any(word in user_lower for word in ["hola", "buenos", "saludos", "buenas"]):
        return random.choice(templates_t1["saludo"])
    elif any(word in user_lower for word in ["ayuda", "como", "que puedes"]):
        return random.choice(templates_t1["ayuda"])
    elif any(word in user_lower for word in ["adios", "hasta", "bye", "gracias"]):
        return random.choice(templates_t1["despedida"])
    return random.choice(templates_t1["default"])


if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown("### 💬 Chat")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Escribe tu mensaje...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = get_response_t1(prompt)
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

st.markdown("---")
st.markdown("""
### Acerca de este Template

**Template 1: Basic Assistant**

Este es un agente simple que funciona sin API key,
usando respuestas predefinidas basadas en templates.

**Arquitectura:**
```
User Input -> Template Matcher -> Response
```
""")
