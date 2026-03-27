"""
Memory Agent - Template 9: Recipe Box
Arquitectura: Conversation Memory
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Memory T9", page_icon="🍳")

st.title("🍳 Recipe Box")
st.markdown("**Arquitectura:** Conversation Memory | **Modo:** Caja de Recetas")

st.markdown("---")

if "recipes" not in st.session_state:
    st.session_state.recipes = {
        "breakfast": [],
        "lunch": [],
        "dinner": [],
        "dessert": [],
        "snack": [],
    }

st.markdown("### Nueva Receta")

meal_type = st.selectbox(
    "Tipo de comida:", ["Desayuno", "Almuerzo", "Cena", "Postre", "Bocadillo"]
)
recipe_name = st.text_input("Nombre de la receta:")
ingredients = st.text_area("Ingredientes (uno por linea):", height=100)
instructions = st.text_area("Instrucciones:", height=150)
prep_time = st.number_input("Tiempo de preparacion (minutos):", 5, 180, 30)

if st.button("Guardar receta") and recipe_name:
    type_key = {
        "Desayuno": "breakfast",
        "Almuerzo": "lunch",
        "Cena": "dinner",
        "Postre": "dessert",
        "Bocadillo": "snack",
    }[meal_type]

    st.session_state.recipes[type_key].append(
        {
            "name": recipe_name,
            "ingredients": ingredients,
            "instructions": instructions,
            "prep_time": prep_time,
        }
    )
    st.success("Receta guardada!")

st.markdown("---")
st.markdown("### Recetas por Categoria")

categories = {
    "breakfast": "Desayuno",
    "lunch": "Almuerzo",
    "dinner": "Cena",
    "dessert": "Postre",
    "snack": "Bocadillo",
}

for cat_key, cat_name in categories.items():
    recipes = st.session_state.recipes.get(cat_key, [])
    if recipes:
        with st.expander(f"🍽️ {cat_name} ({len(recipes)})"):
            for recipe in recipes:
                with st.expander(f"📖 {recipe['name']}"):
                    st.markdown(f"**Tiempo:** {recipe['prep_time']} min")
                    st.markdown(f"**Ingredientes:**\n{recipe['ingredients']}")
                    st.markdown(f"**Instrucciones:**\n{recipe['instructions']}")

total = sum(len(v) for v in st.session_state.recipes.values())
st.markdown(f"**Total recetas:** {total}")

st.markdown("""
### Acerca de este Template

**Template 9: Recipe Box**

Almacena recetas organizadas por categoria.
""")
