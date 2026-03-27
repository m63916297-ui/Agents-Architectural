import streamlit as st
from dotenv import load_dotenv
from agent import SimpleAgent

load_dotenv()

st.set_page_config(page_title="Simple Agent", page_icon="🤖")

st.title("🤖 Simple Agent")
st.markdown("**Arquitectura:** Single-Agent (Basico)")

if "agent" not in st.session_state:
    st.session_state.agent = SimpleAgent()

if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown("---")
st.markdown("### Configuracion")
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
        with st.spinner("Pensando..."):
            response = st.session_state.agent.run(prompt)
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

st.markdown("---")
st.markdown("""
### Acerca de este Agente

**Arquitectura:** Single-Agent

Este agente implementa el patron mas basico de agente de IA:
- **Entrada:** Mensaje del usuario
- **Proceso:** LLM (GPT-4/GPT-3.5) con prompt de sistema
- **Salida:** Respuesta del modelo

**Componentes:**
- `agent.py`: Logica del agente
- `app.py`: Interfaz Streamlit
""")
