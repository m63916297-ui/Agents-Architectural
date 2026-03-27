"""
Memory Agent - Template 1: Chat History
Arquitectura: Conversation Memory
Sin API Key requerida
"""

import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Memory T1", page_icon="💬")

st.title("💬 Chat History Memory")
st.markdown("**Arquitectura:** Conversation Memory | **Modo:** Historial de Chat")

st.markdown("---")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_msg = st.text_input("Tu mensaje:")
password = st.text_input("Tu contrasena:", type="password")

responses = {
    "hola": "Hola! Como estas hoy?",
    "como estas": "Estoy bien, gracias por preguntar! Y tu?",
    "ayuda": "Estoy aqui para ayudarte. Que necesitas?",
    "adios": "Hasta luego! Fue un placer charlar contigo.",
    "gracias": "De nada! Siempre estoy para ayudarte.",
}

if st.button("Enviar"):
    if user_msg:
        timestamp = datetime.now().strftime("%H:%M")
        st.session_state.chat_history.append(
            {"role": "user", "content": user_msg, "time": timestamp}
        )

        user_lower = user_msg.lower()
        response_text = responses.get(user_lower, "Entiendo. Cuentame mas sobre eso.")

        st.session_state.chat_history.append(
            {"role": "assistant", "content": response_text, "time": timestamp}
        )

st.markdown("---")
st.markdown("### Historial de Conversacion")

for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.markdown(f"**Tu [{msg['time']}]:** {msg['content']}")
    else:
        st.markdown(f"**Asistente [{msg['time']}]:** {msg['content']}")

if st.button("Limpiar historial"):
    st.session_state.chat_history = []

st.markdown("---")
st.markdown(f"**Mensajes en memoria:** {len(st.session_state.chat_history)}")

st.markdown("""
### Acerca de este Template

**Template 1: Chat History Memory**

Mantiene historial de conversacion en memoria.
""")
