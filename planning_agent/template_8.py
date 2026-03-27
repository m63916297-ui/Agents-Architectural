"""
Planning Agent - Template 8: Meal Planner
Arquitectura: Plan-and-Solve
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Planning T8", page_icon="🍽️")

st.title("🍽️ Meal Planner")
st.markdown("**Arquitectura:** Plan-and-Solve | **Modo:** Planificador de Comidas")

st.markdown("---")

meals = {
    "Desayuno": [
        "Avena con frutas",
        "Huevos revueltos",
        "Tostadas integrales",
        "Yogur con granola",
        "Smoothie de frutas",
    ],
    "Almuerzo": [
        "Ensalada cesar",
        "Pollo a la plancha",
        "Sopa de verduras",
        "Arroz con frijoles",
        "Pasta integral",
    ],
    "Cena": [
        "Pescado al horno",
        "Verduras salteadas",
        "Salmón con quinoa",
        "Tacos de pescado",
        "Crema de calabaza",
    ],
    "Snack": ["Frutas", "Nueces", "Yogur", "Palitos de verduras", "Chocolate oscuro"],
}

if "weekly_menu" not in st.session_state:
    st.session_state.weekly_menu = {}

days = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

st.markdown("### Planificador Semanal de Comidas")

selected_day = st.selectbox("Dia:", days)
selected_meal = st.selectbox("Comida:", list(meals.keys()))

st.markdown(f"#### Opciones para {selected_meal}:")
for option in meals[selected_meal]:
    st.markdown(f"- {option}")

if st.button("Asignar comida aleatoria"):
    import random

    chosen = random.choice(meals[selected_meal])
    if selected_day not in st.session_state.weekly_menu:
        st.session_state.weekly_menu[selected_day] = {}
    st.session_state.weekly_menu[selected_day][selected_meal] = chosen
    st.success(f"Asignado: {chosen}")

st.markdown("---")
st.markdown("### Menu de la Semana")

for day in days:
    if day in st.session_state.weekly_menu:
        with st.expander(f"**{day}**"):
            for meal, food in st.session_state.weekly_menu[day].items():
                st.markdown(f"**{meal}:** {food}")

st.markdown("---")
st.markdown("### Lista de Compras")

if "shopping_list" not in st.session_state:
    st.session_state.shopping_list = []

ingredient = st.text_input("Ingrediente a agregar:")

if st.button("Agregar a lista") and ingredient:
    st.session_state.shopping_list.append(ingredient)

for item in st.session_state.shopping_list:
    st.checkbox(item)

st.markdown("""
### Acerca de este Template

**Template 8: Meal Planner**

Planifica comidas semanales con lista de compras.
""")
