"""
Tool Agent - Template 9: Random Generator
Arquitectura: ReAct (Tool Use)
Sin API Key requerida
"""

import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="Tool T9", page_icon="🎲")

st.title("🎲 Random Generator")
st.markdown("**Arquitectura:** ReAct (Tool Use) | **Modo:** Generador Aleatorio")

st.markdown("---")

tabs = st.tabs(["Numero", "Fecha", "Color", "Nombre", "Boolean"])

with tabs[0]:
    st.markdown("### Generador de Numeros")

    min_val = st.number_input("Minimo:", value=1)
    max_val = st.number_input("Maximo:", value=100)
    count = st.number_input("Cantidad:", value=1, min_value=1, max_value=10)

    if st.button("Generar numeros"):
        numbers = [random.randint(min_val, max_val) for _ in range(count)]
        st.success(f"### Numeros generados: {numbers}")

with tabs[1]:
    st.markdown("### Generador de Fecha")

    start_date = st.date_input("Desde:")
    end_date = st.date_input("Hasta:")

    if st.button("Generar fecha"):
        delta = end_date - start_date
        random_days = random.randint(0, delta.days)
        random_date = start_date + timedelta(days=random_days)
        st.success(f"### Fecha generada: {random_date}")

with tabs[2]:
    st.markdown("### Generador de Color")

    colors = [
        "Rojo",
        "Azul",
        "Verde",
        "Amarillo",
        "Naranja",
        "Morado",
        "Rosa",
        "Negro",
        "Blanco",
    ]

    if st.button("Generar color"):
        color = random.choice(colors)
        st.success(f"### Color generado: {color}")

with tabs[3]:
    st.markdown("### Generador de Nombre")

    names = [
        "Carlos",
        "Maria",
        "Juan",
        "Ana",
        "Pedro",
        "Laura",
        "Miguel",
        "Sofia",
        "David",
        "Emma",
    ]
    surnames = [
        "Garcia",
        "Rodriguez",
        "Martinez",
        "Lopez",
        "Gonzalez",
        "Hernandez",
        "Perez",
        "Sanchez",
    ]

    if st.button("Generar nombre"):
        name = f"{random.choice(names)} {random.choice(surnames)}"
        st.success(f"### Nombre generado: {name}")

with tabs[4]:
    st.markdown("### Generador Boolean")

    if st.button("Lanzar moneda"):
        result = random.choice(["Cara", "Cruz"])
        st.success(f"### Resultado: {result}")

    if st.button("Si o No"):
        result = random.choice([True, False])
        st.markdown(f"### Resultado: {'Si' if result else 'No'}")

st.markdown("---")
st.markdown("### Lista Aleatoria")

items = st.text_area("Elementos (uno por linea):").split("\n")
items = [i for i in items if i.strip()]

if st.button("Mezclar lista") and items:
    random.shuffle(items)
    for item in items:
        st.markdown(f"- {item}")

st.markdown("""
### Acerca de este Template

**Template 9: Random Generator**

Genera elementos aleatorios de diferentes tipos.
""")
