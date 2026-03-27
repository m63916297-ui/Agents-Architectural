"""
Simple Agent - Template 5: Translator/Formatter
Arquitectura: Single-Agent
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Simple Agent T5", page_icon="🔄")

st.title("🔄 Text Transformer")
st.markdown("**Arquitectura:** Single-Agent | **Modo:** Transformador de Texto")

st.markdown("---")

transformations = {
    "MAYUSCULAS": lambda x: x.upper(),
    "minusculas": lambda x: x.lower(),
    "Titulo": lambda x: x.title(),
    "Sin tildes": lambda x: (
        x.replace("á", "a")
        .replace("é", "e")
        .replace("í", "i")
        .replace("ó", "o")
        .replace("ú", "u")
        .replace("Á", "A")
        .replace("É", "E")
        .replace("Í", "I")
        .replace("Ó", "O")
        .replace("Ú", "U")
    ),
    "Sin espacios": lambda x: x.replace(" ", ""),
    "Primera letra": lambda x: x[0].upper() + x[1:] if len(x) > 0 else x,
    "Invertir": lambda x: x[::-1],
    "Longitud": lambda x: (
        f"El texto tiene {len(x)} caracteres y {len(x.split())} palabras"
    ),
    "Contar palabras": lambda x: f"Palabras: {len(x.split())}",
    "Lineas": lambda x: f"Lineas: {len(x.split(chr(10)))}",
}

text_input = st.text_area("Texto a transformar:", height=150)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Transformaciones Rapidas")
    for name in list(transformations.keys())[:5]:
        if st.button(name, use_container_width=True):
            if text_input:
                result = transformations[name](text_input)
                st.session_state.last_result = result

with col2:
    st.markdown("### Transformaciones Avanzadas")
    for name in list(transformations.keys())[5:]:
        if st.button(name, use_container_width=True):
            if text_input:
                result = transformations[name](text_input)
                st.session_state.last_result = result

if "last_result" in st.session_state:
    st.markdown("---")
    st.markdown("### Resultado")
    st.code(st.session_state.last_result)

st.markdown("---")
st.markdown("### Resumen Rapido")
if text_input:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Caracteres", len(text_input))
    with col2:
        st.metric("Palabras", len(text_input.split()))
    with col3:
        st.metric("Lineas", len(text_input.split("\n")))
    with col4:
        st.metric("Vocales", sum(1 for c in text_input.lower() if c in "aeiou"))

st.markdown("""
### Acerca de este Template

**Template 5: Text Transformer**

Conjunto de herramientas para transformar y analizar texto.
""")
