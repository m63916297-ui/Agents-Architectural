import streamlit as st
import os
from dotenv import load_dotenv
from agent import PlanningAgent

load_dotenv()

st.set_page_config(page_title="Planning Agent", page_icon="📋")

st.title("📋 Planning Agent")
st.markdown("**Arquitectura:** Plan-and-Solve / Task Decomposition")

if "agent" not in st.session_state:
    st.session_state.agent = PlanningAgent()

st.markdown("---")
st.markdown("### Configuración")
model = st.selectbox("Modelo:", ["gpt-4", "gpt-3.5-turbo"])
temp = st.slider("Temperatura:", 0.0, 1.0, 0.3, 0.1)

if st.button("Actualizar Agente"):
    st.session_state.agent = PlanningAgent(model_name=model, temperature=temp)
    st.success("Agente actualizado!")

st.markdown("---")
st.markdown("### Planificación de Tareas")

goal = st.text_area(
    "Objetivo a planificar:",
    placeholder="Ej: Crear una aplicación web de gestión de tareas con Python y Flask...",
    height=100,
)

col1, col2 = st.columns(2)

with col1:
    plan_only = st.button("📋 Solo Planificar", use_container_width=True)

with col2:
    plan_and_execute = st.button("🚀 Planificar y Ejecutar", use_container_width=True)

if plan_only and goal:
    with st.spinner("Creando plan..."):
        result = st.session_state.agent.create_plan(goal)

    st.markdown("### 📝 Plan Creado")
    st.markdown(result["plan"])
    st.success("Plan creado exitosamente!")

if plan_and_execute and goal:
    with st.spinner("Planificando y ejecutando..."):
        result = st.session_state.agent.plan_and_execute(goal)

    st.markdown("### 📋 Plan")
    st.markdown(result["plan"])

    st.markdown("### ⚡ Ejecución")
    st.markdown(result["execution"])

    st.success("Objetivo completado!")

st.markdown("---")
st.markdown("""
### 📖 Acerca de este Agente

**Arquitectura:** Plan-and-Solve / Task Decomposition

Este agente implementa capacidades de planificación:

1. **ENTENDER**: Comprende el objetivo final
2. **DESCOMPONER**: Divide en sub-metas manejables
3. **ORDENAR**: Establece dependencias y orden
4. **EJECUTAR**: Completa cada paso
5. **VERIFICAR**: Confirma el cumplimiento

**Referencia:** "Plan-and-solve prompting" - Arxiv 2305.04091
""")
