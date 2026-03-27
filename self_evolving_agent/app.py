import streamlit as st
from dotenv import load_dotenv
from agent import SelfEvolvingAgent

load_dotenv()

st.set_page_config(page_title="Self-Evolving Agent", page_icon="🧬")

st.title("🧬 Self-Evolving Agent")
st.markdown("**Arquitectura:** Auto-Evolucion con Retroalimentacion")

if "agent" not in st.session_state:
    st.session_state.agent = SelfEvolvingAgent()

st.markdown("---")
st.markdown("### Estado de Evolucion")

if st.button("📊 Ver Estado de Evolucion"):
    status = st.session_state.agent.get_evolution_status()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Interacciones", status["interactions"])
    with col2:
        st.metric("Mejoras Aprendidas", status["improvements_count"])
    with col3:
        st.metric("Longitud del Prompt", f"{status['system_prompt_length']} chars")

    if status["recent_improvements"]:
        st.markdown("#### Ultimas Mejoras")
        for i, imp in enumerate(status["recent_improvements"], 1):
            with st.expander(f"Mejora {i}"):
                st.markdown(imp)

if st.button("💭 Reflexionar sobre Desempeno"):
    with st.spinner("Reflexionando..."):
        reflection = st.session_state.agent.reflect_on_performance()
    st.markdown("### Reflexion")
    st.markdown(reflection)

st.markdown("---")
st.markdown("### Chat con Auto-Evolucion")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "pending_feedback" not in st.session_state:
    st.session_state.pending_feedback = ""

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
            feedback = (
                st.session_state.pending_feedback
                if st.session_state.pending_feedback
                else None
            )
            result = st.session_state.agent.run(prompt, feedback)

        st.markdown(result["response"])

        if result.get("learning"):
            st.markdown("### 📝 Aprendizaje")
            st.info(result["learning"])

        if result.get("reflection"):
            st.markdown("### 💭 Reflexion")
            st.markdown(result["reflection"])

    st.session_state.messages.append(
        {"role": "assistant", "content": result["response"]}
    )
    st.session_state.pending_feedback = ""

st.markdown("---")
st.markdown("### Retroalimentacion")

feedback = st.text_area(
    "Retroalimentacion (se aplicara en la proxima interaccion):",
    placeholder="Ej: Podrias ser mas especifico en...",
    key="feedback_input",
)

if st.button("Guardar Retroalimentacion"):
    st.session_state.pending_feedback = feedback
    st.success("Retroalimentacion guardada!")

st.markdown("---")
st.markdown("""
### Acerca de este Agente

**Arquitectura:** Self-Evolving Agent

Este agente implementa auto-evolucion:

1. **Ejecutar**: Procesa la interaccion normalmente
2. **Evaluar**: Auto-evalua su desempeno
3. **Aprender**: Incorpora retroalimentacion
4. **Actualizar**: Mejora su system prompt
5. **Reflexionar**: Analiza su progreso

**Referencia:** "Self-Consolidation for Self-Evolving Agents" - Arxiv 2602.01966
""")
