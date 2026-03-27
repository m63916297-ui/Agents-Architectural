"""
Tool Agent - Template 2: Unit Converter
Arquitectura: ReAct (Tool Use)
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Tool T2", page_icon="🔄")

st.title("🔄 Unit Converter")
st.markdown("**Arquitectura:** ReAct (Tool Use) | **Modo:** Conversor de Unidades")

st.markdown("---")

conversions = {
    "Longitud": {
        "Metro": 1,
        "Kilometro": 0.001,
        "Centimetro": 100,
        "Milimetro": 1000,
        "Pulgada": 39.3701,
        "Pie": 3.28084,
        "Milla": 0.000621371,
    },
    "Peso": {
        "Kilogramo": 1,
        "Gramo": 1000,
        "Miligramo": 1000000,
        "Libra": 2.20462,
        "Onza": 35.274,
    },
    "Temperatura": {"Celsius": 1, "Fahrenheit": 1, "Kelvin": 1},
    "Volumen": {
        "Litro": 1,
        "Mililitro": 1000,
        "Galon": 0.264172,
        "Metro cubico": 0.001,
    },
    "Tiempo": {
        "Segundo": 1,
        "Minuto": 1 / 60,
        "Hora": 1 / 3600,
        "Dia": 1 / 86400,
        "Semana": 1 / 604800,
    },
}

st.markdown("### Seleccionar Categoria")

category = st.selectbox("Categoria:", list(conversions.keys()))

col1, col2 = st.columns(2)

with col1:
    from_unit = st.selectbox("De:", list(conversions[category].keys()))

with col2:
    to_unit = st.selectbox("A:", list(conversions[category].keys()))

value = st.number_input("Valor:", value=1.0)

if st.button("Convertir"):
    if category == "Temperatura":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = value * 9 / 5 + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (value - 32) * 5 / 9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = value + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = value - 273.15
        else:
            result = value
    else:
        result = (
            value * conversions[category][to_unit] / conversions[category][from_unit]
        )

    st.success(f"**{value} {from_unit} = {result:.4f} {to_unit}**")

st.markdown("---")
st.markdown("### Tabla de Referencia Rapida")

for cat, units in conversions.items():
    with st.expander(f"{cat}"):
        for unit in units:
            st.markdown(f"- {unit}")

st.markdown("""
### Acerca de este Template

**Template 2: Unit Converter**

Convierte entre diferentes unidades de medida.
""")
