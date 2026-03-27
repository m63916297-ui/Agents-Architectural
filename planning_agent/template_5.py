"""
Planning Agent - Template 5: Travel Planner
Arquitectura: Plan-and-Solve
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Planning T5", page_icon="✈️")

st.title("✈️ Travel Planner")
st.markdown("**Arquitectura:** Plan-and-Solve | **Modo:** Planificador de Viajes")

st.markdown("---")

if "travel_plan" not in st.session_state:
    st.session_state.travel_plan = {}

st.markdown("### Informacion del Viaje")

destination = st.text_input("Destino:")
travel_date = st.date_input("Fecha de viaje:")
duration = st.selectbox(
    "Duracion:", ["Fin de semana", "1 semana", "2 semanas", "1 mes"]
)

if destination:
    st.session_state.travel_plan["destination"] = destination
    st.session_state.travel_plan["date"] = str(travel_date)
    st.session_state.travel_plan["duration"] = duration

st.markdown("---")

tabs = st.tabs(["Transporte", "Alojamiento", "Actividades", "Equipaje", "Presupuesto"])

with tabs[0]:
    st.markdown("### Opciones de Transporte")
    transport = st.selectbox("Tipo:", ["Avion", "Tren", "Autobus", "Auto", "Barco"])
    cost = st.number_input("Costo estimado:", value=0.0)
    if st.button("Agregar transporte"):
        st.success(f"Transporte agregado: {transport} - ${cost}")

with tabs[1]:
    st.markdown("### Alojamiento")
    hotel = st.text_input("Nombre del hotel/lugar:")
    nights = st.number_input("Noches:", 1, 30, 3)
    nightly_cost = st.number_input("Costo por noche:", value=0.0)
    total_hotel = nights * nightly_cost
    st.metric("Total alojamiento", f"${total_hotel}")

with tabs[2]:
    st.markdown("### Actividades Planificadas")
    for i in range(5):
        activity = st.text_input(f"Actividad {i + 1}:", key=f"activity_{i}")
        activity_cost = st.number_input(f"Costo:", value=0.0, key=f"activity_cost_{i}")
        activity_day = st.selectbox(
            f"Dia:", [f"Dia {j + 1}" for j in range(7)], key=f"activity_day_{i}"
        )

with tabs[3]:
    st.markdown("### Lista de Equipaje")
    essentials = [
        "Pasaporte/DNI",
        "Billetes",
        "Tarjetas",
        "Telefono",
        "Cargador",
        "Ropa interior",
        "Ropa de clima",
    ]

    packed = {}
    for item in essentials:
        packed[item] = st.checkbox(item)

    packed_count = sum(packed.values())
    st.progress(packed_count / len(essentials))
    st.markdown(f"Packed: {packed_count}/{len(essentials)}")

with tabs[4]:
    st.markdown("### Presupuesto Estimado")
    st.metric("Transporte", "$0")
    st.metric("Alojamiento", f"${total_hotel if 'total_hotel' in dir() else 0}")
    st.metric("Comida ($30/dia)", f"${duration_map.get(duration, 7) * 30}")
    st.metric("Actividades", "$0")

    st.markdown("**Total estimado:** $0")

st.markdown("""
### Acerca de este Template

**Template 5: Travel Planner**

Planifica viajes con diferentes categorias.
""")
