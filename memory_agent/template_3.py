"""
Memory Agent - Template 3: Context Keeper
Arquitectura: Conversation Memory
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Memory T3", page_icon="🔗")

st.title("🔗 Context Keeper")
st.markdown("**Arquitectura:** Conversation Memory | **Modo:** Mantenedor de Contexto")

st.markdown("---")

if "context" not in st.session_state:
    st.session_state.context = {
        "current_topic": "",
        "topics_discussed": [],
        "key_points": [],
    }

st.markdown("### Tema Actual")

current_topic = st.text_input(
    "Tema de conversacion actual:",
    value=st.session_state.context.get("current_topic", ""),
)

if st.button("Establecer tema") and current_topic:
    st.session_state.context["current_topic"] = current_topic
    if current_topic not in st.session_state.context["topics_discussed"]:
        st.session_state.context["topics_discussed"].append(current_topic)

st.markdown("---")
st.markdown("### Puntos Clave")

key_point = st.text_input("Agregar punto clave:")
if st.button("Agregar punto") and key_point:
    st.session_state.context["key_points"].append(key_point)

for i, point in enumerate(st.session_state.context.get("key_points", [])):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(f"- {point}")
    with col2:
        if st.button("X", key=f"del_point_{i}"):
            st.session_state.context["key_points"].pop(i)
            st.rerun()

st.markdown("---")
st.markdown("### Temas Discutidos")
for topic in st.session_state.context.get("topics_discussed", []):
    if topic == st.session_state.context.get("current_topic"):
        st.markdown(f"📌 {topic}")
    else:
        st.markdown(f"- {topic}")

st.markdown(
    f"**Contexto activo:** {st.session_state.context.get('current_topic', 'Ninguno')}"
)

st.markdown("""
### Acerca de este Template

**Template 3: Context Keeper**

Mantiene el contexto de la conversacion.
""")
