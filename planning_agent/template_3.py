"""
Planning Agent - Template 3: Goal Tracker
Arquitectura: Plan-and-Solve
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Planning T3", page_icon="🎯")

st.title("🎯 Goal Tracker")
st.markdown("**Arquitectura:** Plan-and-Solve | **Modo:** Seguimiento de Metas")

st.markdown("---")

if "goals" not in st.session_state:
    st.session_state.goals = []

st.markdown("### Nueva Meta")

goal_name = st.text_input("Nombre de la meta:")
goal_deadline = st.date_input("Fecha limite:")
goal_importance = st.slider("Importancia (1-10):", 1, 10, 5)

subgoals = []
for i in range(5):
    sg = st.text_input(f"Submeta {i + 1}:", key=f"sg_{i}")
    if sg:
        subgoals.append({"name": sg, "done": False})

if st.button("Crear Meta") and goal_name:
    st.session_state.goals.append(
        {
            "name": goal_name,
            "deadline": str(goal_deadline),
            "importance": goal_importance,
            "subgoals": subgoals,
            "done": False,
        }
    )
    st.success("Meta creada!")

st.markdown("---")
st.markdown("### Metas Activas")

for i, goal in enumerate(st.session_state.goals):
    if not goal["done"]:
        with st.expander(f"🎯 {goal['name']} (Importancia: {goal['importance']})"):
            st.markdown(f"**Fecha limite:** {goal['deadline']}")

            completed = sum(1 for sg in goal["subgoals"] if sg["done"])
            total = len(goal["subgoals"])
            if total > 0:
                progress = completed / total
                st.progress(progress)
                st.markdown(f"Progreso: {completed}/{total} submeltas")

            for j, sg in enumerate(goal["subgoals"]):
                col1, col2 = st.columns([1, 4])
                with col1:
                    checked = st.checkbox("", value=sg["done"], key=f"goal_{i}_sg_{j}")
                    if checked != sg["done"]:
                        st.session_state.goals[i]["subgoals"][j]["done"] = checked
                        st.rerun()
                with col2:
                    st.markdown(
                        f"☐ {sg['name']}" if not sg["done"] else f"✅ {sg['name']}"
                    )

            if st.button("Completar Meta", key=f"done_{i}"):
                st.session_state.goals[i]["done"] = True
                st.rerun()

            if st.button("Eliminar Meta", key=f"del_goal_{i}"):
                st.session_state.goals.pop(i)
                st.rerun()

st.markdown("""
### Acerca de este Template

**Template 3: Goal Tracker**

Sigue tus metas con submeltas.
""")
