"""
Reasoning Agent - Template 2: Math Problems
Arquitectura: Chain-of-Thought
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Reasoning T2", page_icon="🔢")

st.title("🔢 Math Problem Solver")
st.markdown("**Arquitectura:** Chain-of-Thought | **Modo:** Problemas Matematicos")

st.markdown("---")

math_problems = {
    "ecuaciones": {
        "title": "Resolver Ecuaciones",
        "problems": [
            {"eq": "2x + 5 = 15", "steps": ["2x = 15 - 5", "2x = 10", "x = 10 / 2", "x = 5"], "answer": "x = 5"},
            {"eq": "3x - 7 = 14", "steps": ["3x = 14 + 7", "3x = 21", "x = 21 / 3", "x = 7"], "answer": "x = 7"},
            {"eq": "5x + 3 = 2x + 18", "steps": ["5x - 2x = 18 - 3", "3x = 15", "x = 15 / 3", "x = 5"], "answer": "x = 5"}
        ]
    },
    "porcentajes": {
        "title": "Problemas de Porcentaje",
        "problems": [
            {"eq": "El 20% de que numero es 50?", "steps": ["20% x N = 50", "0.20 x N = 50", "N = 50 / 0.20", "N = 250"], "answer": "250"},
            {"eq": "Un producto cuesta $80 y sube 15%. Cual es el nuevo precio?", "steps": ["Aumento = 80 x 0.15 = 12", "Nuevo precio = 80 + 12 = 92"], "answer": "$92"}
        ]
    },
    "secuencias": {
        "title": "Secuencias Numericas",
        "problems": [
            {"eq": "2, 6, 18, 54, ?", "steps": ["6/2 = 3", "18/6 = 3", "54/18 = 3", "El patron es x3"], "answer": "54 x 3 = 162"},
            {"eq": "1, 1, 2, 3, 5, 8, ?", "steps": ["1+1=2", "1+2=3", "2+3=5", "3+5=8", "Fibonacci"], "answer": "5 + 8 = 13"}
        ]
    }
}

category = st.selectbox("Categoria:", list(math_problems.keys()))
problem_list = math_problems[category]["problems"]
problem = st.selectbox("Problema:", [""] + list(range(len(problem_list)))

if problem != "" and problem < len(problem_list):
    prob = problem_list[problem]
    st.markdown(f"### {prob['eq']}")
    
    if st.button("Mostrar pasos"):
        st.markdown("#### Paso a paso:")
        for i, step in enumerate(prob['steps'], 1):
            st.markdown(f"{i}. {step}")
    
    if st.button("Mostrar respuesta"):
        st.success(f"Respuesta: {prob['answer']}")

st.markdown("---")
st.markdown("### Calculadora Rapida")

col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("Numero 1:", value=0.0)
with col2:
    num2 = st.number_input("Numero 2:", value=0.0)

operation = st.selectbox("Operacion:", ["+", "-", "*", "/", "% de"])

if st.button("Calcular"):
    if operation == "+":
        st.success(f"{num1} + {num2} = {num1 + num2}")
    elif operation == "-":
        st.success(f"{num1} - {num2} = {num1 - num2}")
    elif operation == "*":
        st.success(f"{num1} * {num2} = {num1 * num2}")
    elif operation == "/":
        if num2 != 0:
            st.success(f"{num1} / {num2} = {num1 / num2}")
        else:
            st.error("No se puede dividir por cero")
    elif operation == "% de":
        st.success(f"{num2}% de {num1} = {num1 * num2 / 100}")

st.markdown("""
### Acerca de este Template

**Template 2: Math Problem Solver**

Resuelve problemas matematicos paso a paso.
""")
