"""
Reasoning Agent - Template 4: Cause & Effect
Arquitectura: Chain-of-Thought
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Reasoning T4", page_icon="🔗")

st.title("🔗 Cause & Effect Analyzer")
st.markdown("**Arquitectura:** Chain-of-Thought | **Modo:** Analisis de Causa y Efecto")

st.markdown("---")

examples = {
    "cambio_climatico": {
        "causas": [
            "Emisiones de CO2 por combustion de fosiles",
            "Deforestacion masiva",
            "Industria ganadera",
            "Transporte contaminante",
            "Produccion industrial",
        ],
        "efectos": [
            "Aumento de temperatura global",
            "Derretimiento de glaciares",
            "Eventos climaticos extremos",
            "Subida del nivel del mar",
            "Perdida de biodiversidad",
        ],
        "solutions": [
            "Transicion a energias renovables",
            "Reforestacion masiva",
            "Transporte publico electrico",
            "Economia circular",
            "Conciencia ambiental",
        ],
    },
    "tecnologia": {
        "causas": [
            "Avance de la inteligencia artificial",
            "Digitalizacion acelerada",
            "Acceso a internet movil",
            "Reduccion de costos de dispositivos",
            "Pandemia global",
        ],
        "efectos": [
            "Trabajo remoto mas comun",
            "Cambio en patrones de consumo",
            "Automatizacion de tareas",
            "Nueva economia digital",
            "Cambios en educacion",
        ],
        "solutions": [
            "Educacion digital inclusiva",
            "Regulacion de IA",
            "Alfabetizacion tecnologica",
            "Balance vida-trabajo",
            "Proteccion de datos",
        ],
    },
}

st.markdown("### Selecciona un Tema")
topic = st.selectbox("Tema:", [""] + list(examples.keys()))

if topic:
    data = examples[topic]

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 🔴 Causas")
        for cause in data["causas"]:
            st.markdown(f"- {cause}")

    with col2:
        st.markdown("#### 🔵 Efectos")
        for effect in data["efectos"]:
            st.markdown(f"- {effect}")

    st.markdown("---")
    st.markdown("#### 🟢 Posibles Soluciones")
    for sol in data["solutions"]:
        st.markdown(f"- {sol}")

    st.markdown("---")
    st.markdown("#### Cadena de Causa-Efecto")

    for i, (cause, effect) in enumerate(
        zip(data["causas"][:3], data["efectos"][:3]), 1
    ):
        st.markdown(f"{i}. **{cause}**")
        st.markdown(f"   ↓")
        st.markdown(f"   **{effect}**")
        st.markdown("")

st.markdown("---")
st.markdown("### Crea tu Propio Analisis")

custom_cause = st.text_input("Causa:")
custom_effect = st.text_input("Efecto:")

if custom_cause and custom_effect:
    st.markdown("### Tu Cadena de Causa-Efecto")
    st.error(f"CAUSA: {custom_cause}")
    st.markdown("↓")
    st.markdown("↓")
    st.markdown("↓")
    st.success(f"EFECTO: {custom_effect}")

st.markdown("""
### Acerca de este Template

**Template 4: Cause & Effect Analyzer**

Visualiza relaciones de causa y efecto.
""")
