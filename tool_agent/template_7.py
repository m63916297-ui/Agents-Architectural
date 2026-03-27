"""
Tool Agent - Template 7: Time Zone Converter
Arquitectura: ReAct (Tool Use)
Sin API Key requerida
"""

import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Tool T7", page_icon="🌍")

st.title("🌍 Time Zone Converter")
st.markdown(
    "**Arquitectura:** ReAct (Tool Use) | **Modo:** Conversor de Zonas Horarias"
)

st.markdown("---")

timezones = {
    "Londres": 0,
    "Paris": 1,
    "Madrid": 1,
    "Nueva York": -5,
    "Los Angeles": -8,
    "Tokio": 9,
    "Pekin": 8,
    "Sydney": 11,
    "Buenos Aires": -3,
    "Mexico DF": -6,
    "Sao Paulo": -3,
    "Moscu": 3,
}

st.markdown("### Seleccionar Zonas")

col1, col2 = st.columns(2)

with col1:
    from_zone = st.selectbox("Zona de origen:", list(timezones.keys()))

with col2:
    to_zone = st.selectbox("Zona de destino:", list(timezones.keys()))

local_time = st.time_input("Hora local:", value=datetime.now().time())

if st.button("Convertir"):
    diff = timezones[to_zone] - timezones[from_zone]

    from_dt = datetime.combine(datetime.today(), local_time)
    to_dt = from_dt.replace(hour=(from_dt.hour + diff) % 24)

    st.success(f"### Resultado")
    st.markdown(
        f"**{from_zone} ({local_time})** = **{to_zone} ({to_dt.strftime('%H:%M')})**"
    )

    if diff > 0:
        st.markdown(f"{to_zone} esta {diff} horas adelante")
    elif diff < 0:
        st.markdown(f"{to_zone} esta {abs(diff)} horas atras")
    else:
        st.markdown("Ambas zonas tienen la misma hora")

st.markdown("---")
st.markdown("### Hora Actual en Diferentes Zonas")

now = datetime.now()
for zone, offset in timezones.items():
    zone_time = (now.hour + offset) % 24
    with st.expander(f"{zone}"):
        st.markdown(f"**Hora:** {zone_time:02d}:{now.minute:02d}")
        st.markdown(f"**Diferencia con UTC:** {offset:+.0f} horas")

st.markdown("""
### Acerca de este Template

**Template 7: Time Zone Converter**

Convierte horas entre diferentes zonas horarias.
""")
