"""
Planning Agent - Template 10: Career Development
Arquitectura: Plan-and-Solve
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Planning T10", page_icon="🚀")

st.title("🚀 Career Development Planner")
st.markdown("**Arquitectura:** Plan-and-Solve | **Modo:** Plan de Carrera")

st.markdown("---")

if "career_plan" not in st.session_state:
    st.session_state.career_plan = {
        "current_role": "",
        "target_role": "",
        "skills": [],
        "milestones": [],
    }

st.markdown("### Informacion de Carrera")

current_role = st.text_input("Rol actual:")
target_role = st.text_input("Rol objetivo:")
timeline = st.selectbox("Timeline:", ["6 meses", "1 ano", "2 anos", "5 anos"])

if current_role and target_role:
    st.session_state.career_plan["current_role"] = current_role
    st.session_state.career_plan["target_role"] = target_role

st.markdown("---")
st.markdown("### Habilidades a Desarrollar")

skill = st.text_input("Nueva habilidad:")
skill_priority = st.selectbox("Prioridad:", ["Critica", "Importante", "Nice-to-have"])

if st.button("Agregar Habilidad") and skill:
    st.session_state.career_plan["skills"].append(
        {"name": skill, "priority": skill_priority, "learned": False}
    )

for i, s in enumerate(st.session_state.career_plan["skills"]):
    col1, col2, col3 = st.columns([1, 3, 1])
    with col1:
        checked = st.checkbox("", value=s["learned"], key=f"skill_{i}")
        if checked != s["learned"]:
            st.session_state.career_plan["skills"][i]["learned"] = checked
    with col2:
        priority_color = {"Critica": "🔴", "Importante": "🟡", "Nice-to-have": "🟢"}
        st.markdown(f"{priority_color[s['priority']]} {s['name']}")
    with col3:
        if st.button("X", key=f"del_skill_{i}"):
            st.session_state.career_plan["skills"].pop(i)
            st.rerun()

st.markdown("---")
st.markdown("### Hitos del Plan")

milestone = st.text_input("Hito/Milenstone:")
milestone_date = st.date_input("Fecha objetivo:")

if st.button("Agregar Hito") and milestone:
    st.session_state.career_plan["milestones"].append(
        {"name": milestone, "date": str(milestone_date), "done": False}
    )

for i, m in enumerate(st.session_state.career_plan["milestones"]):
    col1, col2, col3 = st.columns([1, 3, 1])
    with col1:
        checked = st.checkbox("", value=m["done"], key=f"milestone_{i}")
        if checked != m["done"]:
            st.session_state.career_plan["milestones"][i]["done"] = checked
    with col2:
        st.markdown(f"{'✅' if m['done'] else '⬜'} **{m['name']}** - {m['date']}")
    with col3:
        if st.button("X", key=f"del_milestone_{i}"):
            st.session_state.career_plan["milestones"].pop(i)
            st.rerun()

st.markdown("---")
st.markdown("### Roadmap de Transicion")

if current_role and target_role:
    st.markdown(f"""
    #### De **{current_role}** a **{target_role}**
    
    1. **Fase 1 (0-3 meses)**: Adquirir habilidades basicas
    2. **Fase 2 (3-6 meses)**: Practicar y aplicar conocimientos
    3. **Fase 3 (6-12 meses)**: Construir portfolio/proyectos
    4. **Fase 4 (12+ meses)**: Buscar oportunidades y transicion
    """)

st.markdown("""
### Acerca de este Template

**Template 10: Career Development Planner**

Planifica tu desarrollo profesional.
""")
