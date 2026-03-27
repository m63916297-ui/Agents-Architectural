"""
Memory Agent - Template 6: Idea Bank
Arquitectura: Conversation Memory
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Memory T6", page_icon="💡")

st.title("💡 Idea Bank")
st.markdown("**Arquitectura:** Conversation Memory | **Modo:** Banco de Ideas")

st.markdown("---")

if "ideas" not in st.session_state:
    st.session_state.ideas = {"saved": [], "implemented": []}

st.markdown("### Nueva Idea")

idea = st.text_area("Describe tu idea:")
category = st.selectbox(
    "Categoria:", ["Proyecto", "Mejora", "Solucion", "Concepto", "Otro"]
)

if st.button("Guardar idea") and idea:
    st.session_state.ideas["saved"].append({"idea": idea, "category": category})
    st.success("Idea guardada!")

st.markdown("---")

tabs = st.tabs(["Ideas Guardadas", "Implementadas", "Descartadas"])

with tabs[0]:
    st.markdown("### Ideas Pendientes")
    for i, item in enumerate(st.session_state.ideas["saved"]):
        with st.expander(f"💡 {item['idea'][:50]}..."):
            st.markdown(f"**Categoria:** {item['category']}")
            st.markdown(f"**Idea completa:** {item['idea']}")

            col1, col2 = st.columns(2)
            with col1:
                if st.button("Implementar", key=f"impl_{i}"):
                    st.session_state.ideas["implemented"].append(item)
                    st.session_state.ideas["saved"].pop(i)
                    st.rerun()
            with col2:
                if st.button("Descartar", key=f"disc_{i}"):
                    st.session_state.ideas["saved"].pop(i)
                    st.rerun()

with tabs[1]:
    st.markdown("### Ideas Implementadas")
    for item in st.session_state.ideas["implemented"]:
        st.markdown(f"✅ {item['idea'][:100]}...")

with tabs[2]:
    st.markdown("### Estadisticas")
    st.metric("Guardadas", len(st.session_state.ideas["saved"]))
    st.metric("Implementadas", len(st.session_state.ideas["implemented"]))

st.markdown("""
### Acerca de este Template

**Template 6: Idea Bank**

Guarda y gestiona ideas con estados.
""")
