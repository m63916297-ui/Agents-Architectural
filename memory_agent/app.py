import streamlit as st
from dotenv import load_dotenv
from agent import MemoryAgent

load_dotenv()

st.set_page_config(page_title="Memory Agent", page_icon="🧠")

st.title("🧠 Memory Agent")
st.markdown("**Arquitectura:** Conversation Memory (Buffer)")

if "agent" not in st.session_state:
    st.session_state.agent = MemoryAgent()

if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown("---")
st.markdown("### Configuracion")
model = st.selectbox("Modelo:", ["gpt-4", "gpt-3.5-turbo"])
memory_limit = st.slider("Limite de memoria (intercambios):", 5, 20, 10)

if st.button("Actualizar Agente"):
    st.session_state.agent = MemoryAgent(model_name=model, memory_limit=memory_limit)
    st.success("Agente actualizado!")

col1, col2 = st.columns(2)
with col1:
    if st.button("📜 Ver Memoria"):
        history = st.session_state.agent.get_memory()
        if history:
            st.session_state.show_memory = True
        else:
            st.info("Memoria vacia")

with col2:
    if st.button("🗑️ Limpiar Memoria"):
        st.session_state.agent.clear_memory()
        st.session_state.messages = []
        st.success("Memoria limpiada!")

if st.session_state.get("show_memory", False):
    st.markdown("### 📝 Memoria Actual")
    history = st.session_state.agent.get_memory()
    for i, msg in enumerate(history):
        role = "👤" if msg["role"] == "user" else "🤖"
        st.markdown(f"{role}: {msg['content'][:200]}...")

st.markdown("---")
st.markdown("### Chat Conversacional")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Escribe tu mensaje..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Pensando con memoria..."):
            response = st.session_state.agent.run(prompt)
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

st.markdown("---")
st.markdown("""
### Acerca de este Agente

**Arquitectura:** Conversation Memory

Este agente implementa gestion de memoria:

- **Short-term:** Mantiene historial de conversacion reciente
- **Contextual:** Recuerda informacion de mensajes previos
- **Limite:** Limita memoria para eficiencia

**Referencia:** "MemGPT: Towards LLMs as Operating Systems" - Arxiv 2310.08560
""")
