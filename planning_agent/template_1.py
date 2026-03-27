"""
Planning Agent - Template 1: Project Planner
Arquitectura: Plan-and-Solve
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Planning T1", page_icon="📋")

st.title("📋 Project Planner")
st.markdown("**Arquitectura:** Plan-and-Solve | **Modo:** Planificador de Proyectos")

st.markdown("---")

st.markdown("### Define tu Proyecto")

project_name = st.text_input("Nombre del proyecto:")
project_goal = st.text_area("Objetivo principal:", height=80)
timeline = st.selectbox(
    "Duracion estimada:",
    ["1 semana", "2 semanas", "1 mes", "3 meses", "6 meses", "1 ano"],
)

if project_name and project_goal:
    st.markdown("---")
    st.markdown(f"### Plan: {project_name}")

    phases = {
        "1 semana": 3,
        "2 semanas": 4,
        "1 mes": 5,
        "3 meses": 6,
        "6 meses": 8,
        "1 ano": 12,
    }

    num_phases = phases.get(timeline, 5)

    for i in range(num_phases):
        phase_name = st.text_input(f"Fase {i + 1}:", key=f"phase_{i}")
        if phase_name:
            with st.expander(f"Fase {i + 1}: {phase_name}"):
                tasks = st.text_area(
                    f"Tareas de {phase_name}:", height=100, key=f"tasks_{i}"
                )
                if tasks:
                    task_list = [t.strip() for t in tasks.split("\n") if t.strip()]
                    for j, task in enumerate(task_list, 1):
                        st.markdown(f"  {j}. {task}")

st.markdown("""
### Acerca de este Template

**Template 1: Project Planner**

Planifica proyectos con fases y tareas.
""")
