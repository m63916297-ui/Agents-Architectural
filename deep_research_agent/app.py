import streamlit as st
import os
from dotenv import load_dotenv
from agent import DeepResearchAgent

load_dotenv()

st.set_page_config(page_title="Deep Research Agent", page_icon="📚")

st.title("📚 Deep Research Agent")
st.markdown("**Arquitectura:** Investigación Profunda con Verificación")

if "agent" not in st.session_state:
    st.session_state.agent = DeepResearchAgent()

st.markdown("---")
st.markdown("### Configuración")
model = st.selectbox("Modelo:", ["gpt-4", "gpt-3.5-turbo"])

st.markdown("---")
st.markdown("### Investigación Profunda")

query = st.text_area(
    "Consulta de investigación:",
    placeholder="Ej: Impacto de la inteligencia artificial en el mercado laboral global...",
    height=100,
)

if st.button("🔬 Ejecutar Investigación Profunda", use_container_width=True) and query:
    results = st.session_state.agent.deep_research(query)

    st.success("¡Investigación completada!")

    st.markdown("### 📋 Subtemas Investigados")
    for i, subtopic in enumerate(results["subtopics"], 1):
        st.markdown(f"- **{i}.** {subtopic}")

    st.markdown("### 📊 Fuentes Recopiladas")
    for src in results["research_data"][:10]:
        st.markdown(f"- **{src['title']}** ({src.get('source', 'Unknown')})")

    st.markdown("### ✅ Verificación")
    st.markdown(
        results["verifications"][0]
        if results["verifications"]
        else "Sin verificaciones"
    )

    st.markdown("---")
    st.markdown("### 📑 REPORTE FINAL")
    st.markdown(results["report"])

st.markdown("---")
st.markdown("""
### 📖 Acerca de este Agente

**Arquitectura:** Deep Research Agent

Este agente implementa investigación profunda:

1. **Planificación**: Descompone la consulta en subtemas
2. **Investigación Iterativa**: Explora múltiples fuentes
3. **Verificación**: Valida la información recopilada
4. **Síntesis**: Genera reportes comprehensivos

**Referencia:** "Deep Research: A Systematic Survey" - Arxiv 2512.02038
""")
