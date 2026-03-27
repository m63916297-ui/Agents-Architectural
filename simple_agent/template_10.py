"""
Simple Agent - Template 10: Random Picker/Raffle
Arquitectura: Single-Agent
Sin API Key requerida
"""

import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="Simple Agent T10", page_icon="🎲")

st.title("🎲 Random Picker & Raffle")
st.markdown("**Arquitectura:** Single-Agent | **Modo:** Sorteos y Selecciones")

st.markdown("---")

tab1, tab2, tab3 = st.tabs(["Selector Aleatorio", "Sorteo", "Ruleta"])

with tab1:
    st.markdown("### Selector de Opciones")

    if "random_options" not in st.session_state:
        st.session_state.random_options = []

    new_option = st.text_input("Nueva opcion:")
    if st.button("Agregar opcion"):
        if new_option:
            st.session_state.random_options.append(new_option)
            st.rerun()

    if st.button("🗑️ Limpiar todo"):
        st.session_state.random_options = []
        st.rerun()

    st.markdown("#### Opciones:")
    for i, opt in enumerate(st.session_state.random_options):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"- {opt}")
        with col2:
            if st.button("X", key=f"del_{i}"):
                st.session_state.random_options.pop(i)
                st.rerun()

    if len(st.session_state.random_options) >= 2 and st.button("🎯 Seleccionar"):
        selected = random.choice(st.session_state.random_options)
        st.balloons()
        st.success(f"## {selected}")
        st.markdown(f"Seleccionado de {len(st.session_state.random_options)} opciones")

with tab2:
    st.markdown("### Sorteo")

    participants = st.text_area("Participantes (uno por linea):", height=200)
    num_winners = st.number_input("Numero de ganadores:", 1, 10, 1)

    if st.button("🎰 Realizar Sorteo") and participants:
        lines = [l.strip() for l in participants.split("\n") if l.strip()]
        if len(lines) >= num_winners:
            winners = random.sample(lines, num_winners)
            st.markdown("### Ganadores:")
            for i, winner in enumerate(winners, 1):
                st.markdown(f"🥇 #{i}: {winner}")
        else:
            st.error("No hay suficientes participantes")

with tab3:
    st.markdown("### Ruleta de Suerte")

    if "roulette_items" not in st.session_state:
        st.session_state.roulette_items = ["Premio 1", "Premio 2", "Premio 3"]

    new_prize = st.text_input("Nuevo elemento:")
    if st.button("Agregar a ruleta"):
        if new_prize:
            st.session_state.roulette_items.append(new_prize)
            st.rerun()

    if st.button("🌀 Girar ruleta"):
        result = random.choice(st.session_state.roulette_items)
        st.markdown("---")
        st.markdown("---")
        st.markdown("---")
        st.markdown(f"## 🎉 {result} 🎉")

    st.markdown("### Elementos de la ruleta:")
    cols = st.columns(3)
    for i, item in enumerate(st.session_state.roulette_items):
        with cols[i % 3]:
            st.markdown(f"- {item}")

st.markdown("---")
st.markdown("""
### Acerca de este Template

**Template 10: Random Picker & Raffle**

Herramientas para seleccion aleatoria y sorteos.
""")
