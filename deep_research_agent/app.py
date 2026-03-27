import streamlit as st
from dotenv import load_dotenv
from agent import DeepResearchAgent

load_dotenv()

st.set_page_config(page_title="Deep Research Agent", page_icon="📚")

st.title("📚 Deep Research Agent")
st.markdown("**Arquitectura:** Investigacion Profunda con Verificacion")

if "agent" not in st.session_state:
    st.session_state.agent = DeepResearchAgent()

st.markdown("---")
st.markdown("### Configuracion")
model = st.selectbox("Modelo:", ["gpt-4", "gpt-3.5-turbo"])

st.markdown("---")
st.markdown("### Investigacion Profunda")

query = st.text_area(
    "Consulta de investigacion:",
    placeholder="Ej: Impacto de la inteligencia artificial en el mercado laboral global...",
    height=100,
)

if st.button("🔬 Ejecutar Investigacion Profunda", use_container_width=True) and query:
    results = st.session_state.agent.deep_research(query)

    st.success("¡Investigacion completada!")

    st.markdown("### 📋 Subtemas Investigados")
    for i, subtopic in enumerate(results["subtopics"], 1):
        st.markdown(f"- **{i}.** {subtopic}")

    st.markdown("### 📊 Fuentes Recopiladas")
    for src in results["research_data"][:10]:
        st.markdown(f"- **{src['title']}** ({src.get('source', 'Unknown')})")

    st.markdown("### ✅ Verificacion")
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
### Acerca de este Agente

**Arquitectura:** Deep Research Agent

Este agente implementa investigacion profunda:

1. **Planificacion**: Descompone la consulta en subtemas
2. **Investigacion Iterativa**: Explora multiples fuentes
3. **Verificacion**: Valida la informacion recopilada
4. **Sintesis**: Genera reportes comprehensivos

**Referencia:** "Deep Research: A Systematic Survey" - Arxiv 2512.02038
""")
