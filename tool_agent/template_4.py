"""
Tool Agent - Template 4: Timer/Alarm
Arquitectura: ReAct (Tool Use)
Sin API Key requerida
"""

import streamlit as st
import time
from datetime import datetime, timedelta

st.set_page_config(page_title="Tool T4", page_icon="⏰")

st.title("⏰ Timer & Alarm Tool")
st.markdown("**Arquitectura:** ReAct (Tool Use) | **Modo:** Temporizador y Alarma")

st.markdown("---")

if "timer_running" not in st.session_state:
    st.session_state.timer_running = False
    st.session_state.timer_seconds = 0
    st.session_state.timer_start = 0

tabs = st.tabs(["Temporizador", "Alarma", "Cronometro"])

with tabs[0]:
    st.markdown("### Temporizador")

    hours = st.number_input("Horas:", 0, 23, 0)
    minutes = st.number_input("Minutos:", 0, 59, 5)
    seconds = st.number_input("Segundos:", 0, 59, 0)

    total_seconds = hours * 3600 + minutes * 60 + seconds

    if st.button("Iniciar temporizador"):
        st.session_state.timer_running = True
        st.session_state.timer_start = time.time()
        st.session_state.timer_seconds = total_seconds

    if st.session_state.timer_running:
        elapsed = int(time.time() - st.session_state.timer_start)
        remaining = max(0, st.session_state.timer_seconds - elapsed)

        if remaining > 0:
            remaining_h = remaining // 3600
            remaining_m = (remaining % 3600) // 60
            remaining_s = remaining % 60
            st.markdown(f"### ⏰ {remaining_h:02d}:{remaining_m:02d}:{remaining_s:02d}")
            st.rerun()
        else:
            st.success("⏰ Tiempo completado!")
            st.balloons()
            st.session_state.timer_running = False

with tabs[1]:
    st.markdown("### Alarmas Programadas")

    if "alarms" not in st.session_state:
        st.session_state.alarms = []

    alarm_time = st.time_input("Hora de alarma:")
    alarm_label = st.text_input("Etiqueta:", value="Alarma")

    if st.button("Agregar alarma"):
        st.session_state.alarms.append({"time": str(alarm_time), "label": alarm_label})
        st.success("Alarma agregada!")

    for i, alarm in enumerate(st.session_state.alarms):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"⏰ **{alarm['time']}** - {alarm['label']}")
        with col2:
            if st.button("X", key=f"del_alarm_{i}"):
                st.session_state.alarms.pop(i)
                st.rerun()

with tabs[2]:
    st.markdown("### Cronometro")

    if "stopwatch_start" not in st.session_state:
        st.session_state.stopwatch_start = None
        st.session_state.stopwatch_elapsed = 0

    if st.button("Iniciar cronometro"):
        st.session_state.stopwatch_start = time.time()

    if st.button("Detener"):
        if st.session_state.stopwatch_start:
            st.session_state.stopwatch_elapsed = (
                time.time() - st.session_state.stopwatch_start
            )

    if st.button("Reiniciar"):
        st.session_state.stopwatch_start = None
        st.session_state.stopwatch_elapsed = 0

    if st.session_state.stopwatch_start:
        elapsed = time.time() - st.session_state.stopwatch_start
    else:
        elapsed = st.session_state.stopwatch_elapsed

    hours = int(elapsed // 3600)
    minutes = int((elapsed % 3600) // 60)
    seconds = int(elapsed % 60)

    st.markdown(f"### ⏱️ {hours:02d}:{minutes:02d}:{seconds:02d}")

st.markdown("""
### Acerca de este Template

**Template 4: Timer & Alarm Tool**

Herramientas de tiempo integradas.
""")
