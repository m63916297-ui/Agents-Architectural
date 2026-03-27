"""
Memory Agent - Template 5: Learning Journal
Arquitectura: Conversation Memory
Sin API Key requerida
"""

import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Memory T5", page_icon="📓")

st.title("📓 Learning Journal")
st.markdown("**Arquitectura:** Conversation Memory | **Modo:** Diario de Aprendizaje")

st.markdown("---")

if "journal" not in st.session_state:
    st.session_state.journal = []

st.markdown("### Nueva Entrada")

date = st.date_input("Fecha:")
learned = st.text_area("Que aprendi hoy?", height=100)
tags = st.multiselect(
    "Etiquetas:",
    ["Programacion", "Matematicas", "Ciencia", "Arte", "Negocios", "Idioma", "Otro"],
)

if st.button("Guardar entrada") and learned:
    st.session_state.journal.append(
        {"date": str(date), "content": learned, "tags": tags}
    )
    st.success("Entrada guardada!")

st.markdown("---")
st.markdown("### Entradas del Diario")

filter_tag = st.selectbox(
    "Filtrar por etiqueta:",
    ["Todas"]
    + list(
        set(tag for entry in st.session_state.journal for tag in entry.get("tags", []))
    ),
)

for entry in st.session_state.journal[::-1]:
    if filter_tag == "Todas" or filter_tag in entry.get("tags", []):
        with st.expander(f"📅 {entry['date']}"):
            st.markdown(entry["content"])
            tags_str = ", ".join(entry.get("tags", []))
            if tags_str:
                st.markdown(f"*Etiquetas: {tags_str}*")

st.markdown(f"**Total entradas:** {len(st.session_state.journal)}")

st.markdown("""
### Acerca de este Template

**Template 5: Learning Journal**

Registra y filtra aprendizados diarios.
""")
