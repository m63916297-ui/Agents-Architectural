"""
Reasoning Agent - Template 9: Analogies Builder
Arquitectura: Chain-of-Thought
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Reasoning T9", page_icon="🔄")

st.title("🔄 Analogies Builder")
st.markdown("**Arquitectura:** Chain-of-Thought | **Modo:** Constructor de Analogias")

st.markdown("---")

analogies = {
    "tecnologia": [
        {
            "a": "Internet",
            "like": "Biblioteca infinita",
            "because": "Contiene informacion accesible a todos",
        },
        {
            "a": "IA",
            "like": "Asistente digital",
            "because": "Ayuda con tareas repetitivas",
        },
        {
            "a": "Smartphone",
            "like": "Navaja suiza moderna",
            "because": "Tiene multiples herramientas en un dispositivo",
        },
    ],
    "naturaleza": [
        {
            "a": "Cerebro",
            "like": "Ciudad conectada",
            "because": "Millones de neuronas se comunican como calles y edificios",
        },
        {
            "a": "Ecosistema",
            "like": "Orquesta",
            "because": "Cada especie tiene un rol como un instrumento musical",
        },
        {
            "a": "DNA",
            "like": "Codigo fuente",
            "because": "Contiene las instrucciones para crear un organismo",
        },
    ],
    "social": [
        {
            "a": "Familia",
            "like": "Equipo",
            "because": "Cada miembro tiene roles pero trabajan juntos",
        },
        {
            "a": "Democracia",
            "like": "Mercado de ideas",
            "because": "Cada voto cuenta como una opinion",
        },
        {
            "a": "Educacion",
            "like": "Jardin",
            "because": "El conocimiento crece con cuidado y tiempo",
        },
    ],
}

st.markdown("### Analogias Predefinidas")

category = st.selectbox("Categoria:", [""] + list(analogies.keys()))

if category:
    for i, analogy in enumerate(analogies[category], 1):
        with st.expander(f"Analogia {i}"):
            st.markdown(f"**{analogy['a']}** es como **'{analogy['like']}'**")
            st.markdown(f"_Porque:_ {analogy['because']}")

st.markdown("---")
st.markdown("### Crea tu Propia Analogy")

concept = st.text_input("Concepto a explicar:")
like_concept = st.text_input("Es como...")
because = st.text_area("Por que son similares?")

if concept and like_concept and because:
    st.markdown("---")
    st.markdown("### Tu Analogy")
    st.info(f"**{concept}** es como **'{like_concept}'**")
    st.markdown(f"_Porque:_ {because}")

st.markdown("---")
st.markdown("""
### Estructura de una Buena Analogy

1. **Concepto conocido**: Algo que tu audiencia ya entiende
2. **Concepto nuevo**: Lo que quieres explicar
3. **Similitud**: El punto en comun clave
4. **Limitaciones**: Donde termina la comparacion
""")

st.markdown("""
### Acerca de este Template

**Template 9: Analogies Builder**

Construye analogias para explicar conceptos complejos.
""")
