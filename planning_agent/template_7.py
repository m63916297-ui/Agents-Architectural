"""
Planning Agent - Template 7: Event Planning
Arquitectura: Plan-and-Solve
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Planning T7", page_icon="🎉")

st.title("🎉 Event Planner")
st.markdown("**Arquitectura:** Plan-and-Solve | **Modo:** Planificador de Eventos")

st.markdown("---")

if "events" not in st.session_state:
    st.session_state.events = []

st.markdown("### Nuevo Evento")

event_name = st.text_input("Nombre del evento:")
event_date = st.date_input("Fecha:")
event_guests = st.number_input("Numero de invitados:", 1, 500, 50)
event_type = st.selectbox("Tipo:", ["Fiesta", "Reunion", "Conferencia", "Boda", "Otro"])

if st.button("Crear Evento") and event_name:
    st.session_state.events.append(
        {
            "name": event_name,
            "date": str(event_date),
            "guests": event_guests,
            "type": event_type,
            "tasks": [],
        }
    )

st.markdown("---")

for i, event in enumerate(st.session_state.events):
    with st.expander(f"🎊 {event['name']} - {event['date']}"):
        st.markdown(f"**Tipo:** {event['type']}")
        st.markdown(f"**Invitados:** {event['guests']}")

        st.markdown("#### Tareas:")
        task = st.text_input("Nueva tarea:", key=f"task_{i}")
        if st.button("Agregar tarea") and task:
            st.session_state.events[i]["tasks"].append({"name": task, "done": False})
            st.rerun()

        for j, t in enumerate(event["tasks"]):
            col1, col2 = st.columns([1, 4])
            with col1:
                checked = st.checkbox("", value=t["done"], key=f"event_{i}_task_{j}")
                if checked != t["done"]:
                    st.session_state.events[i]["tasks"][j]["done"] = checked
            with col2:
                st.markdown(f"{'✅' if t['done'] else '☐'} {t['name']}")

st.markdown("---")
st.markdown("### Checklist General")

checklist = [
    "Contratar proveedores",
    "Enviar invitaciones",
    "Confirmar asistencia",
    "Preparar menu",
    "Decoracion",
    "Musica/Entretenimiento",
    "Fotografo",
    "Limpieza post-evento",
]

for item in checklist:
    st.checkbox(item)

st.markdown("""
### Acerca de este Template

**Template 7: Event Planner**

Planifica eventos con tareas y checklist.
""")
