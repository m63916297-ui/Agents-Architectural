"""
Simple Agent - Template 7: Code Snippets Generator
Arquitectura: Single-Agent
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Simple Agent T7", page_icon="💻")

st.title("💻 Code Snippets Generator")
st.markdown("**Arquitectura:** Single-Agent | **Modo:** Generador de Codigo")

st.markdown("---")

code_snippets = {
    "python": {
        "hello": """print("Hello, World!")""",
        "funcion": '''def nombre_funcion(parametro):
    """Docstring de la funcion"""
    resultado = parametro * 2
    return resultado''',
        "clase": '''class MiClase:
    def __init__(self, valor):
        self.valor = valor
    
    def metodo(self):
        return f"El valor es {self.valor}"''',
        "list_comprehension": """numeros = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in numeros]""",
        "dict_comprehension": """claves = ["a", "b", "c"]
valores = [1, 2, 3]
mi_dict = {k: v for k, v in zip(claves, valores)}""",
    },
    "javascript": {
        "hello": 'console.log("Hello, World!");',
        "funcion": """function nombreFuncion(parametro) {
    return parametro * 2;
}""",
        "arrow": """const flecha = (a, b) => a + b;""",
        "array_methods": """const nums = [1, 2, 3, 4, 5];
const doubles = nums.map(n => n * 2);
const evens = nums.filter(n => n % 2 === 0);""",
        "async": """async function fetchData() {
    const response = await fetch(url);
    const data = await response.json();
    return data;
}""",
    },
    "html": {
        "basic": """<!DOCTYPE html>
<html>
<head><title>Titulo</title></head>
<body><h1>Hola Mundo</h1></body>
</html>""",
        "form": """<form action="/submit" method="POST">
    <input type="text" name="nombre" placeholder="Nombre">
    <button type="submit">Enviar</button>
</form>""",
        "table": """<table>
    <tr><th>Nombre</th><th>Edad</th></tr>
    <tr><td>Juan</td><td>25</td></tr>
</table>""",
    },
    "css": {
        "basic": """selector {
    propiedad: valor;
    color: #333;
}""",
        "flexbox": """.container {
    display: flex;
    justify-content: center;
    align-items: center;
}""",
        "grid": """.grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 20px;
}""",
    },
    "sql": {
        "select": """SELECT columna1, columna2
FROM tabla
WHERE condicion;""",
        "join": """SELECT *
FROM tabla1
INNER JOIN tabla2 ON tabla1.id = tabla2.foreign_id;""",
        "group": """SELECT columna, COUNT(*)
FROM tabla
GROUP BY columna
HAVING COUNT(*) > 1;""",
    },
}

language = st.selectbox("Lenguaje:", list(code_snippets.keys()))
snippet_type = st.selectbox(
    "Tipo de snippet:", list(code_snippets.get(language, {}).keys())
)

if language in code_snippets and snippet_type in code_snippets[language]:
    st.code(code_snippets[language][snippet_type], language=language)

st.markdown("---")
st.markdown("### Explorar Snippets")

selected_lang = st.selectbox("Ver todos los snippets de:", list(code_snippets.keys()))

for name, code in code_snippets.get(selected_lang, {}).items():
    with st.expander(f"Ver: {name}"):
        st.code(code, language=selected_lang)

st.markdown("""
### Acerca de este Template

**Template 7: Code Snippets Generator**

Biblioteca de fragmentos de codigo predefinidos.
""")
