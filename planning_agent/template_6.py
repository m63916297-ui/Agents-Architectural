"""
Planning Agent - Template 6: Study Plan
Arquitectura: Plan-and-Solve
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Planning T6", page_icon="📚")

st.title("📚 Study Plan")
st.markdown("**Arquitectura:** Plan-and-Solve | **Modo:** Plan de Estudio")

st.markdown("---")

if "study_plan" not in st.session_state:
    st.session_state.study_plan = []

st.markdown("### Agregar Materia/Tema")

subject = st.text_input("Materia/Tema:")
chapters = st.number_input("Numero de capitulos/temas:", 1, 50, 5)
hours_per_chapter = st.number_input("Horas por capitulo:", 1.0, 20.0, 2.0)
deadline = st.date_input("Fecha de examen/evaluacion:")

if st.button("Crear Plan de Estudio") and subject:
    days = (deadline - st.date.today()).days
    if days > 0:
        daily_hours = (chapters * hours_per_chapter) / days
    else:
        daily_hours = chapters * hours_per_chapter

    st.session_state.study_plan.append(
        {
            "subject": subject,
            "chapters": chapters,
            "hours": hours_per_chapter,
            "deadline": str(deadline),
            "daily_hours": daily_hours,
        }
    )

st.markdown("---")
st.markdown("### Plan de Estudios")

for i, plan in enumerate(st.session_state.study_plan):
    with st.expander(f"📖 {plan['subject']}"):
        st.markdown(f"**Capitulos:** {plan['chapters']}")
        st.markdown(f"**Horas por capitulo:** {plan['hours']}")
        st.markdown(f"**Fecha limite:** {plan['deadline']}")
        st.metric("Horas diarias recomendadas", f"{plan['daily_hours']:.1f}")

        if st.button("Eliminar", key=f"del_study_{i}"):
            st.session_state.study_plan.pop(i)
            st.rerun()

st.markdown("---")
st.markdown("### Tecnicas de Estudio")

techniques = {
    "Pomodoro": "25 min estudio, 5 min descanso, repetir 4 veces, luego 15-30 min descanso",
    "Repeticion Espaciada": "Repasar contenido en intervalos crecientes: 1 dia, 3 dias, 1 semana, 2 semanas",
    " Feynman": "1. Elige un concepto, 2. Explica como si fuera para un nino, 3. Identifica huecos, 4. Simplifica",
    "Mapas Mentales": "Centraliza el tema principal y ramifica conceptos relacionados visualmente",
}

for tech, desc in techniques.items():
    with st.expander(f"📝 {tech}"):
        st.markdown(desc)

st.markdown("""
### Acerca de este Template

**Template 6: Study Plan**

Crea planes de estudio con tecnicas de aprendizaje.
""")
