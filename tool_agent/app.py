import streamlit as st
import os
from dotenv import load_dotenv
from agent import ToolAgent, get_current_time, search_wikipedia, calculate

load_dotenv()

st.set_page_config(page_title="Tool Agent", page_icon="🔧")

st.title("🔧 Tool Agent")
st.markdown("**Arquitectura:** ReAct (Reasoning + Acting)")

if "agent" not in st.session_state:
    st.session_state.agent = ToolAgent()

if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown("---")
st.markdown("### Herramientas Disponibles")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🕐", "Tiempo Actual")
    if st.button("Obtener Tiempo"):
        result = get_current_time()
        st.info(f"Hora actual: {result}")

with col2:
    st.metric("📚", "Wikipedia")
    wiki_query = st.text_input("Buscar:", key="wiki")
    if st.button("Buscar Wikipedia") and wiki_query:
        with st.spinner("Buscando..."):
            result = search_wikipedia(wiki_query)
        st.markdown(result)

with col3:
    st.metric("🔢", "Calculadora")
    calc_expr = st.text_input("Expresión:", key="calc")
    if st.button("Calcular") and calc_expr:
        result = calculate(calc_expr)
        st.info(result)

st.markdown("---")
st.markdown("### Chat con Herramientas")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Escribe tu pregunta..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Procesando..."):
            response = st.session_state.agent.run(prompt)
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

st.markdown("---")
st.markdown("""
### 📖 Acerca de este Agente

**Arquitectura:** ReAct (Reasoning + Acting)

Este agente implementa el ciclo ReAct:

1. **THOUGHT**: ¿Qué necesito hacer?
2. **ACTION**: Seleccionar herramienta
3. **OBSERVATION**: Analizar resultado
4. **RESPONSE**: Responder

**Herramientas:**
- Tiempo Actual
- Wikipedia Search
- Calculadora

**Referencia:** "ReAct: Synergizing Reasoning and Acting in Language Models" - Arxiv 2210.03629
""")
