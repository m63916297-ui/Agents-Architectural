import streamlit as st
import os
from dotenv import load_dotenv
from agent import ReasoningAgent

load_dotenv()

st.set_page_config(page_title="Reasoning Agent", page_icon="🧠")

st.title("🧠 Reasoning Agent")
st.markdown("**Arquitectura:** Chain-of-Thought (CoT)")

if "agent" not in st.session_state:
    st.session_state.agent = ReasoningAgent()

if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown("---")
st.markdown("### Configuración")
model = st.selectbox("Modelo:", ["gpt-4", "gpt-3.5-turbo"], key="model")
temp = st.slider("Temperatura:", 0.0, 1.0, 0.3, 0.1, key="temp")

if st.button("Actualizar Agente", key="update"):
    st.session_state.agent = ReasoningAgent(model_name=model, temperature=temp)
    st.success("Agente actualizado!")

st.markdown("---")
st.markdown("### Razonamiento")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Plantea un problema o pregunta..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Razonando paso a paso..."):
            response = st.session_state.agent.run(prompt)
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

st.markdown("---")
st.markdown("### Razonamiento Estructurado")

col1, col2 = st.columns(2)
with col1:
    problem = st.text_area(
        "Problema:",
        placeholder="Ej: Si tengo 5 manzanas y compro 3 más...",
        key="problem",
    )
with col2:
    domain = st.selectbox(
        "Dominio:",
        ["general", "matemáticas", "lógica", "ciencia", "negocios"],
        key="domain",
    )

if st.button("Razonar Estructuradamente", key="structured"):
    if problem:
        with st.spinner("Analizando..."):
            result = st.session_state.agent.reason_about_problem(problem, domain)

        st.markdown("#### Resultado del Razonamiento")
        st.info(f"**Dominio:** {result['domain']}")
        st.markdown("**Razonamiento:**")
        st.markdown(result["reasoning"])

st.markdown("---")
st.markdown("""
### 📖 Acerca de este Agente

**Arquitectura:** Chain-of-Thought (CoT)

Este agente implementa capacidades de razonamiento paso a paso:

1. **ANALIZAR**: Entiende exactamente qué se pregunta
2. **RAZONAR**: Divide el problema en pasos lógicos  
3. **RESOLVER**: Ejecuta cada paso mostrando el proceso
4. **CONCLUIR**: Resume la respuesta final

**Referencia:** "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" - Arxiv 2201.11903
""")
