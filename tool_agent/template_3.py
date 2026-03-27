"""
Tool Agent - Template 3: Dictionary
Arquitectura: ReAct (Tool Use)
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Tool T3", page_icon="📖")

st.title("📖 Dictionary Tool")
st.markdown("**Arquitectura:** ReAct (Tool Use) | **Modo:** Diccionario")

st.markdown("---")

dictionary = {
    "python": {
        "word": "Python",
        "type": "Sustantivo",
        "definition": "Lenguaje de programacion de alto nivel, interpretado y orientado a objetos.",
        "example": "Python es muy popular para ciencia de datos.",
    },
    "algoritmo": {
        "word": "Algoritmo",
        "type": "Sustantivo",
        "definition": "Conjunto de instrucciones o reglas definidas para resolver un problema.",
        "example": "El algoritmo de busqueda binaria es muy eficiente.",
    },
    "funcion": {
        "word": "Funcion",
        "type": "Sustantivo",
        "definition": "Bloque de codigo reutilizable que realiza una tarea especifica.",
        "example": "Esta funcion calcula la suma de dos numeros.",
    },
    "variable": {
        "word": "Variable",
        "type": "Sustantivo",
        "definition": "Espacio de memoria para almacenar datos.",
        "example": "La variable 'x' contiene el valor 10.",
    },
    "base de datos": {
        "word": "Base de datos",
        "type": "Sustantivo",
        "definition": "Sistema organizado para almacenar y gestionar informacion.",
        "example": "MySQL es una base de datos relacional popular.",
    },
}

st.markdown("### Buscar Palabra")

word = st.text_input("Palabra a buscar:").lower()

if word:
    if word in dictionary:
        entry = dictionary[word]
        st.success(f"### {entry['word']}")
        st.markdown(f"**Tipo:** {entry['type']}")
        st.markdown(f"**Definicion:** {entry['definition']}")
        st.markdown(f"**Ejemplo:** _{entry['example']}_")
    else:
        st.warning(f"Palabra '{word}' no encontrada en el diccionario.")

st.markdown("---")
st.markdown("### Diccionario Tecnologico")

for term, info in dictionary.items():
    with st.expander(f"📚 {info['word']}"):
        st.markdown(f"**Tipo:** {info['type']}")
        st.markdown(f"**Definicion:** {info['definition']}")

st.markdown("""
### Acerca de este Template

**Template 3: Dictionary Tool**

Busca definiciones en un diccionario integrado.
""")
