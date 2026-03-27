"""
Planning Agent - Template 2: Weekly Planner
Arquitectura: Plan-and-Solve
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Planning T2", page_icon="📅")

st.title("📅 Weekly Planner")
st.markdown("**Arquitectura:** Plan-and-Solve | **Modo:** Planificador Semanal")

st.markdown("---")

days = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

if "weekly_tasks" not in st.session_state:
    st.session_state.weekly_tasks = {day: [] for day in days}

st.markdown("### Planificador Semanal")

selected_day = st.selectbox("Dia:", days)

task = st.text_input("Nueva tarea:")
priority = st.selectbox("Prioridad:", ["Alta", "Media", "Baja"])

if st.button("Agregar tarea") and task:
    st.session_state.weekly_tasks[selected_day].append(
        {"task": task, "priority": priority, "done": False}
    )

st.markdown("---")

for day in days:
    tasks = st.session_state.weekly_tasks[day]
    if tasks:
        with st.expander(f"**{day}** ({len(tasks)} tareas)"):
            for i, t in enumerate(tasks):
                col1, col2, col3 = st.columns([1, 4, 1])
                with col1:
                    checked = st.checkbox("", value=t["done"], key=f"{day}_{i}")
                    if checked != t["done"]:
                        st.session_state.weekly_tasks[day][i]["done"] = checked
                        st.rerun()
                with col2:
                    status = "~~" if t["done"] else ""
                    priority_color = {"Alta": "🔴", "Media": "🟡", "Baja": "🟢"}
                    st.markdown(
                        f"{priority_color[t['priority']]} {status}{t['task']}{status}"
                    )
                with col3:
                    if st.button("X", key=f"del_{day}_{i}"):
                        st.session_state.weekly_tasks[day].pop(i)
                        st.rerun()

st.markdown("---")
st.markdown("### Resumen de la Semana")

total = sum(len(v) for v in st.session_state.weekly_tasks.values())
done = sum(
    1 for tasks in st.session_state.weekly_tasks.values() for t in tasks if t["done"]
)

st.metric("Total tareas", total)
st.metric("Completadas", done)
if total > 0:
    st.metric("Progreso", f"{(done / total) * 100:.0f}%")

st.markdown("""
### Acerca de este Template

**Template 2: Weekly Planner**

Organiza tareas por dia de la semana.
""")
