"""
Planning Agent - Template 4: Daily Routine
Arquitectura: Plan-and-Solve
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Planning T4", page_icon="⏰")

st.title("⏰ Daily Routine Planner")
st.markdown("**Arquitectura:** Plan-and-Solve | **Modo:** Rutina Diaria")

st.markdown("---")

routine_templates = {
    "productivo": [
        ("6:00", "Despertar y ejercicio"),
        ("7:00", "Desayuno saludable"),
        ("8:00", "Trabajo/Estudio (bloque 1)"),
        ("10:00", "Pausa y descanso"),
        ("10:15", "Trabajo/Estudio (bloque 2)"),
        ("12:00", "Almuerzo"),
        ("13:00", "Trabajo/Estudio (bloque 3)"),
        ("15:00", "Reunion o tarea colaborativa"),
        ("17:00", "Cierre y planificacion del dia siguiente"),
        ("18:00", "Tiempo personal/familia"),
        ("22:00", "Prepararse para dormir"),
    ],
    "estudiante": [
        ("6:30", "Despertar"),
        ("7:00", "Desayuno y preparacion"),
        ("8:00", "Clases/Estudio"),
        ("12:00", "Almuerzo"),
        ("13:00", "Estudio independiente"),
        ("15:00", "Deportes o actividades"),
        ("18:00", "Tarea y repasos"),
        ("21:00", "Tiempo personal"),
        ("22:00", "Dormir"),
    ],
    "saludable": [
        ("6:00", "Ejercicio matutino"),
        ("7:00", "Desayuno nutritivo"),
        ("8:00", "Hidratacion"),
        ("10:00", "Snack saludable"),
        ("12:00", "Almuerzo balanceado"),
        ("14:00", "Paseo o estiramientos"),
        ("16:00", "Snack de frutas"),
        ("18:00", "Cena ligera"),
        ("20:00", "Actividad relajante"),
        ("22:00", "Dormir 7-8 horas"),
    ],
}

st.markdown("### Plantillas de Rutina")

template = st.selectbox(
    "Selecciona una plantilla:", [""] + list(routine_templates.keys())
)

if template:
    for time, activity in routine_templates[template]:
        with st.expander(f"{time} - {activity}"):
            done = st.checkbox("Completado")
            notes = st.text_area("Notas:", key=f"{time}")

st.markdown("---")
st.markdown("### Crea tu Propia Rutina")

if "custom_routine" not in st.session_state:
    st.session_state.custom_routine = []

routine_time = st.text_input("Hora (ej: 08:00):")
routine_activity = st.text_input("Actividad:")

if st.button("Agregar a rutina"):
    if routine_time and routine_activity:
        st.session_state.custom_routine.append((routine_time, routine_activity))

if st.session_state.custom_routine:
    st.markdown("#### Tu Rutina:")
    for time, activity in sorted(st.session_state.custom_routine):
        st.markdown(f"**{time}** - {activity}")

st.markdown("""
### Acerca de este Template

**Template 4: Daily Routine Planner**

Planifica tu rutina diaria con plantillas predefinidas.
""")
