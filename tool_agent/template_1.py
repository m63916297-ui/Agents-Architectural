"""
Tool Agent - Template 1: Weather Tool
Arquitectura: ReAct (Tool Use)
Sin API Key requerida
"""

import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Tool T1", page_icon="🌤️")

st.title("🌤️ Weather Tool")
st.markdown("**Arquitectura:** ReAct (Tool Use) | **Modo:** Informacion del Clima")

st.markdown("---")

weather_templates = {
    "soleado": {
        "temp": "25°C",
        "humedad": "45%",
        "viento": "10 km/h",
        "desc": "Dia despejado y soleado",
    },
    "nublado": {
        "temp": "18°C",
        "humedad": "65%",
        "viento": "15 km/h",
        "desc": "Cielo parcialmente nublado",
    },
    "lluvioso": {
        "temp": "15°C",
        "humedad": "85%",
        "viento": "20 km/h",
        "desc": "Lluvias moderadas durante el dia",
    },
    "tormentoso": {
        "temp": "12°C",
        "humedad": "90%",
        "viento": "40 km/h",
        "desc": "Tormentas electricas previstas",
    },
    "nieve": {
        "temp": "-2°C",
        "humedad": "80%",
        "viento": "25 km/h",
        "desc": "Nevadas ligeras",
    },
}

st.markdown("### Consultar Clima")

city = st.text_input("Ciudad:", value="Madrid")
condition = st.selectbox("Condicion simulada:", list(weather_templates.keys()))

if st.button("Consultar clima"):
    weather = weather_templates[condition]

    st.success(f"### Clima en {city}")
    st.markdown(f"**Condicion:** {weather['desc']}")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Temperatura", weather["temp"])
    col2.metric("Humedad", weather["humedad"])
    col3.metric("Viento", weather["viento"])
    col4.metric("Hora", datetime.now().strftime("%H:%M"))

st.markdown("---")
st.markdown("### Pronostico 5 Dias")

for i in range(5):
    day = (
        datetime.now().replace(hour=0, minute=0, second=0) + timedelta(days=i)
    ).strftime("%A")
    cond = list(weather_templates.keys())[i % len(weather_templates)]
    w = weather_templates[cond]
    with st.expander(f"Dia {i + 1}: {day}"):
        st.markdown(f"**Condicion:** {w['desc']}")
        st.markdown(f"**Temp:** {w['temp']}")

st.markdown("""
### Acerca de este Template

**Template 1: Weather Tool**

Simula consulta de informacion climatica.
""")
