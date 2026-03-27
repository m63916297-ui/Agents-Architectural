"""
Reasoning Agent - Template 8: Comparison Matrix
Arquitectura: Chain-of-Thought
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Reasoning T8", page_icon="📊")

st.title("📊 Comparison Matrix")
st.markdown("**Arquitectura:** Chain-of-Thought | **Modo:** Matriz de Comparacion")

st.markdown("---")

st.markdown("### Selecciona items a comparar")

num_items = st.slider("Numero de items:", 2, 5, 3)
items = []
for i in range(num_items):
    item = st.text_input(f"Item {i + 1}:", key=f"item_{i}")
    if item:
        items.append(item)

criteria = st.multiselect(
    "Criterios de comparacion:",
    ["Precio", "Calidad", "Durabilidad", "Facilidad de uso", "Diseno", "Rendimiento"],
)

if items and criteria:
    st.markdown("---")
    st.markdown("### Matriz de Comparacion")

    col1 = st.columns(len(criteria) + 1)[0]
    with col1:
        st.markdown("**Item**")
        for item in items:
            st.markdown(f"**{item}**")

    scores = {}
    for criterion in criteria:
        cols = st.columns(len(criteria) + 1)
        with cols[criteria.index(criterion)]:
            st.markdown(f"**{criterion}**")
            scores[criterion] = {}
            for item in items:
                score = st.selectbox(
                    f"{item} - {criterion}",
                    ["1", "2", "3", "4", "5"],
                    key=f"{item}_{criterion}",
                )
                scores[criterion][item] = int(score)

    st.markdown("---")
    st.markdown("### Resultados")

    totals = {item: sum(scores[c][item] for c in criteria) for item in items}

    for item in sorted(totals.items(), key=lambda x: x[1], reverse=True):
        if item[0] in items:
            percentage = (item[1] / (5 * len(criteria))) * 100
            st.progress(percentage / 100)
            st.markdown(
                f"**{item[0]}**: {item[1]}/{5 * len(criteria)} puntos ({percentage:.1f}%)"
            )

    best = max(totals.items(), key=lambda x: x[1])
    if best[0] in items:
        st.success(f"🏆 Mejor opcion: {best[0]} con {best[1]} puntos")

st.markdown("""
### Acerca de este Template

**Template 8: Comparison Matrix**

Compara opciones usando criterios ponderados.
""")
