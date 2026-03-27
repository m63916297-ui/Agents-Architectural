import streamlit as st
import os
from dotenv import load_dotenv
from agent import MultiAgentSystem, ResearchAgent, AnalysisAgent, CreativeAgent
from langchain_openai import ChatOpenAI

load_dotenv()

st.set_page_config(page_title="Multi-Agent System", page_icon="🤝")

st.title("🤝 Multi-Agent System")
st.markdown("**Arquitectura:** Sistema Multi-Agente Colaborativo")


@st.cache_resource
def get_llm(model_name: str, temperature: float):
    return ChatOpenAI(model_name=model_name, temperature=temperature)


if "multi_agent" not in st.session_state:
    st.session_state.multi_agent = MultiAgentSystem()

st.markdown("---")
st.markdown("### Configuración")
model = st.selectbox("Modelo:", ["gpt-4", "gpt-3.5-turbo"])

use_all = st.checkbox("Usar todos los agentes", value=True)

st.markdown("---")
st.markdown("### Sistema de Agentes")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### 📚 Investigador")
    st.info("Busca y analiza información de fuentes relevantes")

with col2:
    st.markdown("#### 📊 Analista")
    st.info("Identifica patrones y evalúa alternativas")

with col3:
    st.markdown("#### 💡 Creador")
    st.info("Genera ideas innovadoras")

st.markdown("---")
st.markdown("### Consulta")

query = st.text_area(
    "Ingresa tu consulta o problema:",
    placeholder="Ej: ¿Cuáles son las tendencias en IA para 2025?",
    height=100,
)

if st.button("🚀 Ejecutar Sistema Multi-Agente", use_container_width=True) and query:
    with st.spinner("🤖 Coordinando agentes..."):
        results = st.session_state.multi_agent.run(query, use_all_agents=use_all)

    st.success("¡Procesamiento completado!")

    if use_all:
        with st.expander("📚 Resultado del Investigador"):
            st.markdown(results["agents"]["researcher"])

        with st.expander("📊 Resultado del Analista"):
            st.markdown(results["agents"]["analyst"])

        with st.expander("💡 Resultado del Creador"):
            st.markdown(results["agents"]["creative"])

    st.markdown("### ✅ Síntesis Final")
    st.markdown(results["synthesis"])

st.markdown("---")
st.markdown("""
### 📖 Acerca de este Sistema

**Arquitectura:** Multi-Agent System

Este sistema coordina múltiples agentes especializados:

1. **Investigador**: Busca y analiza información
2. **Analista**: Evalúa patrones y alternativas
3. **Creador**: Genera ideas innovadoras

Los agentes colaboran para proporcionar soluciones integrales.

**Referencia:** "CAMEL: Communicative Agents for Mind Exploration" - Arxiv 2303.17760
""")
