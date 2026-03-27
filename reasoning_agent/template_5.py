"""
Reasoning Agent - Template 5: Hypothesis Tester
Arquitectura: Chain-of-Thought
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Reasoning T5", page_icon="🔬")

st.title("🔬 Hypothesis Tester")
st.markdown("**Arquitectura:** Chain-of-Thought | **Modo:** Prueba de Hipotesis")

st.markdown("---")

st.markdown("### Formula tu Hipotesis")

hypothesis = st.text_area("Escribe tu hipotesis:")

st.markdown("#### Criterios para evaluar:")

criteria = {
    "testable": "Puede ser probada o refutada con evidencia?",
    "especifica": "Es lo suficientemente especifica y clara?",
    "medible": "Puede medirse u observarse?",
    "relevante": "Es relevante para el problema en cuestion?",
}

evaluations = {}
for key, desc in criteria.items():
    st.markdown(f"**{desc}**")
    evaluations[key] = st.selectbox(
        f"Evalua", ["", "Si", "No", "Parcialmente"], key=key
    )

if hypothesis:
    st.markdown("---")
    st.markdown("### Evaluacion de Hipotesis")

    yes_count = sum(1 for v in evaluations.values() if v == "Si")
    partial_count = sum(1 for v in evaluations.values() if v == "Parcialmente")

    if yes_count >= 3:
        st.success("✅ Tu hipotesis parece ser valida!")
    elif yes_count + partial_count >= 3:
        st.warning("⚠️ Tu hipotesis necesita mejoras")
    else:
        st.error("❌ Tu hipotesis requiere revision")

    for key, v in evaluations.items():
        if v == "Si":
            st.markdown(f"✅ {criteria[key]}")
        elif v == "No":
            st.markdown(f"❌ {criteria[key]}")
        elif v == "Parcialmente":
            st.markdown(f"⚠️ {criteria[key]}")

st.markdown("---")
st.markdown("### Metodo Cientifico")

steps = [
    "1. **Observacion**: Observar un fenomeno",
    "2. **Pregunta**: Formular una pregunta",
    "3. **Hipotesis**: Proponer una explicacion",
    "4. **Experimento**: Probar la hipotesis",
    "5. **Analisis**: Analizar los resultados",
    "6. **Conclusion**: Sacar conclusiones",
]

for step in steps:
    st.markdown(step)

st.markdown("""
### Acerca de este Template

**Template 5: Hypothesis Tester**

Evalua hipotesis usando el metodo cientifico.
""")
