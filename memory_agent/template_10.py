"""
Memory Agent - Template 10: Task Memory
Arquitectura: Conversation Memory
Sin API Key requerida
"""

import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="Memory T10", page_icon="✅")

st.title("✅ Task Memory")
st.markdown("**Arquitectura:** Conversation Memory | **Modo:** Memoria de Tareas")

st.markdown("---")

if "tasks" not in st.session_state:
    st.session_state.tasks = {"pending": [], "completed": [], "scheduled": []}

st.markdown("### Nueva Tarea")

task_name = st.text_input("Nombre de la tarea:")
task_priority = st.selectbox("Prioridad:", ["Alta", "Media", "Baja"])
due_date = st.date_input("Fecha limite:")

task_type = st.radio("Tipo de tarea:", ["Pendiente", "Programada"])

if st.button("Agregar tarea") and task_name:
    task = {
        "name": task_name,
        "priority": task_priority,
        "due_date": str(due_date),
        "created": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }

    if task_type == "Pendiente":
        st.session_state.tasks["pending"].append(task)
    else:
        st.session_state.tasks["scheduled"].append(task)

    st.success("Tarea agregada!")

st.markdown("---")

tabs = st.tabs(["Pendientes", "Programadas", "Completadas"])

with tabs[0]:
    st.markdown("### Tareas Pendientes")
    for i, task in enumerate(st.session_state.tasks["pending"]):
        priority_color = {"Alta": "🔴", "Media": "🟡", "Baja": "🟢"}
        with st.expander(f"{priority_color[task['priority']]} {task['name']}"):
            st.markdown(f"**Prioridad:** {task['priority']}")
            st.markdown(f"**Fecha limite:** {task['due_date']}")
            st.markdown(f"**Creada:** {task['created']}")

            col1, col2 = st.columns(2)
            with col1:
                if st.button("Completar", key=f"comp_{i}"):
                    st.session_state.tasks["completed"].append(task)
                    st.session_state.tasks["pending"].pop(i)
                    st.rerun()
            with col2:
                if st.button("Eliminar", key=f"del_p_{i}"):
                    st.session_state.tasks["pending"].pop(i)
                    st.rerun()

with tabs[1]:
    st.markdown("### Tareas Programadas")
    for i, task in enumerate(st.session_state.tasks["scheduled"]):
        with st.expander(f"📅 {task['name']}"):
            st.markdown(f"**Fecha:** {task['due_date']}")

with tabs[2]:
    st.markdown("### Tareas Completadas")
    for task in st.session_state.tasks["completed"][-10:]:
        st.markdown(f"✅ {task['name']} - {task['created']}")

st.markdown("---")
st.markdown("### Estadisticas")
col1, col2, col3 = st.columns(3)
col1.metric("Pendientes", len(st.session_state.tasks["pending"]))
col2.metric("Programadas", len(st.session_state.tasks["scheduled"]))
col3.metric("Completadas", len(st.session_state.tasks["completed"]))

st.markdown("""
### Acerca de este Template

**Template 10: Task Memory**

Gestiona tareas con memoria persistente.
""")
