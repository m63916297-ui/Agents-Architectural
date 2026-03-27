import streamlit as st
import os
from dotenv import load_dotenv
from agent import ResearchAgent

load_dotenv()

st.set_page_config(page_title="Research Agent", page_icon="🔬")

st.title("🔬 Research Agent")
st.markdown("**Arquitectura:** Agentic RAG / Research Agent")

if "agent" not in st.session_state:
    st.session_state.agent = ResearchAgent()

st.markdown("---")
st.markdown("### Configuración")
model = st.selectbox("Modelo:", ["gpt-4", "gpt-3.5-turbo"])

st.markdown("---")
st.markdown("### Investigación")

topic = st.text_input(
    "Tema de investigación:",
    placeholder="Ej: Impacto del cambio climático en la agricultura...",
)

col1, col2 = st.columns(2)

with col1:
    deep = st.checkbox("Investigación profunda")

with col2:
    search = st.button("🔍 Investigar", use_container_width=True)

if search and topic:
    results = st.session_state.agent.research(topic, deep)

    st.success("¡Investigación completada!")

    st.markdown("### 📊 Reporte de Investigación")
    st.markdown(results["report"])

    if results["sources"]:
        st.markdown("### 📚 Fuentes")
        for src in results["sources"][:5]:
            st.markdown(f"- **{src['title']}**")
            if "url" in src:
                st.markdown(f"  [Enlace]({src['url']})")

st.markdown("---")
st.markdown("""
### 📖 Acerca de este Agente

**Arquitectura:** Research Agent / Agentic RAG

Este agente implementa investigación automatizada:

1. **Búsqueda**: Explora múltiples fuentes
2. **Extracción**: Recopila información relevante
3. **Síntesis**: Genera reportes estructurados

**Referencia:** "OpenResearcher: Unleashing AI for Accelerated Scientific Research" - Arxiv 2408.06941
""")
