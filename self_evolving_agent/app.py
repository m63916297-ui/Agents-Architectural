import streamlit as st
import os
from dotenv import load_dotenv
from agent import SelfEvolvingAgent

load_dotenv()

st.set_page_config(page_title="Self-Evolving Agent", page_icon="🧬")

st.title("🧬 Self-Evolving Agent")
st.markdown("**Arquitectura:** Auto-Evolución con Retroalimentación")

if "agent" not in st.session_state:
    st.session_state.agent = SelfEvolvingAgent()

st.markdown("---")
st.markdown("### Estado de Evolución")

if st.button("📊 Ver Estado de Evolución"):
    status = st.session_state.agent.get_evolution_status()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Interacciones", status["interactions"])
    with col2:
        st.metric("Mejoras Aprendidas", status["improvements_count"])
    with col3:
        st.metric("Longitud del Prompt", f"{status['system_prompt_length']} chars")

    if status["recent_improvements"]:
        st.markdown("#### Últimas Mejoras")
        for i, imp in enumerate(status["recent_improvements"], 1):
            with st.expander(f"Mejora {i}"):
                st.markdown(imp)

if st.button("💭 Reflexionar sobre Desempeño"):
    with st.spinner("Reflexionando..."):
        reflection = st.session_state.agent.reflect_on_performance()
    st.markdown("### Reflexión")
    st.markdown(reflection)

st.markdown("---")
st.markdown("### Chat con Auto-Evolución")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "pending_feedback" not in st.session_state:
    st.session_state.pending_feedback = None

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Escribe tu mensaje...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Procesando..."):
            result = st.session_state.agent.run(
                prompt, st.session_state.pending_feedback
            )

        st.markdown(result["response"])

        if result.get("learning"):
            st.markdown("### 📝 Aprendizaje")
            st.info(result["learning"])

        if result.get("reflection"):
            st.markdown("### 💭 Reflexión")
            st.markdown(result["reflection"])

    st.session_state.messages.append(
        {"role": "assistant", "content": result["response"]}
    )
    st.session_state.pending_feedback = None

st.markdown("---")
st.markdown("### Retroalimentación")

feedback = st.text_area(
    "Retroalimentación (se aplicará en la próxima interacción):",
    placeholder="Ej: Podrías ser más específico en...",
)

if st.button("Guardar Retroalimentación"):
    st.session_state.pending_feedback = feedback
    st.success("Retroalimentación guardada!")

st.markdown("---")
st.markdown("""
### 📖 Acerca de este Agente

**Arquitectura:** Self-Evolving Agent

Este agente implementa auto-evolución:

1. **Ejecutar**: Procesa la interacción normalmente
2. **Evaluar**: Auto-evalúa su desempeño
3. **Aprender**: Incorpora retroalimentación
4. **Actualizar**: Mejora su system prompt
5. **Reflexionar**: Analiza su progreso

**Referencia:** "Self-Consolidation for Self-Evolving Agents" - Arxiv 2602.01966
""")
