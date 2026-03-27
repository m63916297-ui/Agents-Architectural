"""
Tool Agent - Template 10: Lorem Ipsum Generator
Arquitectura: ReAct (Tool Use)
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Tool T10", page_icon="📝")

st.title("📝 Lorem Ipsum Generator")
st.markdown("**Arquitectura:** ReAct (Tool Use) | **Modo:** Generador de Texto")

st.markdown("---")

lorem_templates = {
    "breve": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "medio": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation.",
    "largo": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
}

st.markdown("### Generar Texto")

length = st.selectbox("Longitud:", ["breve", "medio", "largo"])

st.markdown(f"**{lorem_templates[length]}**")

st.markdown("---")
st.markdown("### Generador Personalizado")

count = st.slider("Numero de parrafos:", 1, 10, 3)

if st.button("Generar texto"):
    for i in range(count):
        st.markdown(lorem_templates[length])
        st.markdown("")

st.markdown("---")
st.markdown("### Alternativas a Lorem Ipsum")

alternatives = {
    "Bacon Ipsum": "Bacon ipsum dolor amet pork belly tri-tip...",
    "Cupcake Ipsum": "Cupcake ipsum marshmallow danish...",
    "Zombie Ipsum": "Zombie ipsum reversus ab viral...",
    "Pirate Ipsum": "Pirate ipsum ducky deadshots...",
}

for name, sample in alternatives.items():
    with st.expander(name):
        st.markdown(sample[:100] + "...")

st.markdown("""
### Acerca de este Template

**Template 10: Lorem Ipsum Generator**

Genera texto de relleno para disenadores y desarrolladores.
""")
