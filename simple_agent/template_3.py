"""
Simple Agent - Template 3: Task Helper
Arquitectura: Single-Agent
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Simple Agent T3", page_icon="📝")

st.title("📝 Task Helper Agent")
st.markdown("**Arquitectura:** Single-Agent | **Modo:** Asistente de Tareas")

st.markdown("---")

task_templates = {
    "estudiar": {
        "titulo": "Plan de Estudio",
        "pasos": [
            "1. Define objetivos de aprendizaje",
            "2. Crea un horario de estudio",
            "3. Preparar materiales y recursos",
            "4. Tomar notas efectivas",
            "5. Realizar repasos periodicos",
            "6. Evaluar progreso",
        ],
    },
    "proyecto": {
        "titulo": "Plan de Proyecto",
        "pasos": [
            "1. Definir alcance y objetivos",
            "2. Investigar y planificar",
            "3. Disenar la solucion",
            "4. Implementar fase 1",
            "5. Probar y iterar",
            "6. Documentar resultados",
            "7. Presentar conclusion",
        ],
    },
    "reunion": {
        "titulo": "Agenda de Reunion",
        "pasos": [
            "1. Definir objetivo de la reunion",
            "2. Identificar participantes",
            "3. Preparar agenda",
            "4. Enviar invitaciones",
            "5. Realizar la reunion",
            "6. Tomar notas",
            "7. Hacer seguimiento",
        ],
    },
    "default": {
        "titulo": "Plan Generico",
        "pasos": [
            "1. Definir objetivo",
            "2. Investigar opciones",
            "3. Planificar recursos",
            "4. Ejecutar plan",
            "5. Evaluar resultados",
            "6. Ajustar si necesario",
        ],
    },
}

task_type = st.selectbox(
    "Tipo de tarea:", ["", "estudiar", "proyecto", "reunion", "otro"]
)
custom_task = st.text_input("O describe tu propia tarea:")

if st.button("Generar Plan"):
    if task_type and task_type != "otro":
        plan = task_templates.get(task_type, task_templates["default"])
    elif custom_task:
        plan = task_templates["default"]
        plan["titulo"] = f"Plan: {custom_task}"
    else:
        plan = None

    if plan:
        st.success(f"### {plan['titulo']}")
        for paso in plan["pasos"]:
            st.markdown(f"- {paso}")

st.markdown("---")
st.markdown("### To-Do List")

if "todos" not in st.session_state:
    st.session_state.todos = []

col1, col2 = st.columns([3, 1])
with col1:
    new_task = st.text_input("Nueva tarea:")
with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Agregar"):
        if new_task:
            st.session_state.todos.append(new_task)
            st.rerun()

for i, todo in enumerate(st.session_state.todos):
    col1, col2 = st.columns([3, 1])
    with col1:
        st.checkbox(todo, key=f"todo_{i}")
    with col2:
        if st.button("X", key=f"del_{i}"):
            st.session_state.todos.pop(i)
            st.rerun()

st.markdown("""
### Acerca de este Template

**Template 3: Task Helper**

Asistente de planificacion de tareas.
Genera planes estructurados y mantiene lista de tareas.
""")
