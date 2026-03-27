import streamlit as st
from dotenv import load_dotenv
from agent import ResearchAgent

load_dotenv()

st.set_page_config(page_title="Research Agent", page_icon="🔬")

st.title("🔬 Research Agent")
st.markdown("**Arquitectura:** Agentic RAG / Research Agent")

if "agent" not in st.session_state:
    st.session_state.agent = ResearchAgent()

st.markdown("---")
st.markdown("### Configuracion")
model = st.selectbox("Modelo:", ["gpt-4", "gpt-3.5-turbo"])

st.markdown("---")
st.markdown("### Investigacion")

topic = st.text_input(
    "Tema de investigacion:",
    placeholder="Ej: Impacto del cambio climatico en la agricultura...",
)

col1, col2 = st.columns(2)

with col1:
    deep = st.checkbox("Investigacion profunda")

with col2:
    search = st.button("🔍 Investigar", use_container_width=True)

if search and topic:
    results = st.session_state.agent.research(topic, deep)

    st.success("¡Investigacion completada!")

    st.markdown("### 📊 Reporte de Investigacion")
    st.markdown(results["report"])

    if results["sources"]:
        st.markdown("### 📚 Fuentes")
        for src in results["sources"][:5]:
            st.markdown(f"- **{src['title']}**")
            if "url" in src:
                st.markdown(f"  [Enlace]({src['url']})")

st.markdown("---")
st.markdown("""
### Acerca de este Agente

**Arquitectura:** Research Agent / Agentic RAG

Este agente implementa investigacion automatizada:

1. **Busqueda**: Explora multiples fuentes
2. **Extraccion**: Recopila informacion relevante
3. **Sintesis**: Genera reportes estructurados

**Referencia:** "OpenResearcher" - Arxiv 2408.06941
""")
