"""
Memory Agent - Template 7: Meeting Notes
Arquitectura: Conversation Memory
Sin API Key requerida
"""

import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Memory T7", page_icon="📝")

st.title("📝 Meeting Notes Memory")
st.markdown("**Arquitectura:** Conversation Memory | **Modo:** Notas de Reunion")

st.markdown("---")

if "meetings" not in st.session_state:
    st.session_state.meetings = []

st.markdown("### Nueva Reunion")

meeting_title = st.text_input("Titulo de la reunion:")
attendees = st.text_input("Participantes (separados por coma):")
date = st.date_input("Fecha:")
notes = st.text_area("Notas:", height=150)
action_items = st.text_area("Acuerdos/Acciones:", height=100)

if st.button("Guardar reunion") and meeting_title:
    st.session_state.meetings.append(
        {
            "title": meeting_title,
            "attendees": attendees,
            "date": str(date),
            "notes": notes,
            "actions": action_items,
            "created_at": datetime.now().strftime("%H:%M"),
        }
    )
    st.success("Reunion guardada!")

st.markdown("---")
st.markdown("### Reuniones Guardadas")

for meeting in st.session_state.meetings[::-1]:
    with st.expander(f"📅 {meeting['title']} - {meeting['date']}"):
        st.markdown(f"**Participantes:** {meeting['attendees']}")
        st.markdown(f"**Notas:**\n{meeting['notes']}")
        if meeting["actions"]:
            st.markdown(f"**Acuerdos:**\n{meeting['actions']}")

        if st.button(f"Eliminar: {meeting['title']}"):
            st.session_state.meetings.remove(meeting)
            st.rerun()

st.markdown(f"**Total reuniones:** {len(st.session_state.meetings)}")

st.markdown("""
### Acerca de este Template

**Template 7: Meeting Notes Memory**

Guarda notas y acuerdos de reuniones.
""")
