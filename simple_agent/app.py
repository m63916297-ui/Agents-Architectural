import streamlit as st
import os
from dotenv import load_dotenv
from agent import SimpleAgent

load_dotenv()

st.set_page_config(page_title="Simple Agent", page_icon="🤖")

st.title("🤖 Simple Agent")
st.markdown("**Arquitectura:** Single-Agent (Básico)")

if "agent" not in st.session_state:
    st.session_state.agent = SimpleAgent()

if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown("---")
st.markdown("### Configuración")
model = st.selectbox("Modelo:", ["gpt-4", "gpt-3.5-turbo"])
temp = st.slider("Temperatura:", 0.0, 1.0, 0.7, 0.1)

if st.button("Actualizar Agente"):
    st.session_state.agent = SimpleAgent(model_name=model, temperature=temp)
    st.success("Agente actualizado!")

st.markdown("---")
st.markdown("### Chat")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Escribe tu mensaje..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_container = st.empty()
        full_response = ""

        with st.spinner("Pensando..."):
            response = st.session_state.agent.run(prompt)
            full_response = response

        response_container.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})

st.markdown("---")
st.markdown("""
### 📖 Acerca de este Agente

**Arquitectura:** Single-Agent

Este agente implementa el patrón más básico de agente de IA:
- **Entrada:** Mensaje del usuario
- **Proceso:** LLM (GPT-4/GPT-3.5) con prompt de sistema
- **Salida:** Respuesta del modelo

**Componentes:**
- `agent.py`: Lógica del agente
- `app.py`: Interfaz Streamlit
""")
