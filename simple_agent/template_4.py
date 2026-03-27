"""
Simple Agent - Template 4: Idea Generator
Arquitectura: Single-Agent
Sin API Key requerida
"""

import streamlit as st
import random

st.set_page_config(page_title="Simple Agent T4", page_icon="💡")

st.title("💡 Idea Generator")
st.markdown("**Arquitectura:** Single-Agent | **Modo:** Generador de Ideas")

st.markdown("---")

idea_templates = {
    "negocio": [
        "Plataforma de suscripcion para cursos especializados",
        "App de marketplace para productos artesanales locales",
        "Servicio de delivery especializado en productos organicos",
        "Plataforma de freelancing para disenos creativos",
        "App de bienestar corporativo con gamificacion",
    ],
    "app": [
        "App de recetas personalizadas segun ingredientes disponibles",
        "App de organizacion de closet virtual",
        "App de seguimiento de habitos con recompensas",
        "App de traduccion en tiempo real para viajes",
        "App de comparacion de precios entre supermercados",
    ],
    "proyecto": [
        "Sistema de gestion de tareas con IA local",
        "Portfolio interactivo con animaciones",
        "Blog con contenido generado automaticamente",
        "Dashboard de metricas personales",
        "Sistema de reservas para pequenos negocios",
    ],
    "estudio": [
        " Tecnica Pomodoro con estadisticas detalladas",
        "Flashcards con repeticion espaciada",
        "Resumen automatico de articulos academicos",
        "Planner semanal con bloqueo de tiempo",
        "Base de datos de notas interconectadas",
    ],
}

idea_type = st.selectbox(
    "Categoria de idea:", ["", "negocio", "app", "proyecto", "estudio"]
)
generate = st.button("🎲 Generar 5 Ideas")

if generate and idea_type:
    st.markdown(f"### Ideas para: {idea_type.upper()}")
    ideas = idea_templates.get(idea_type, [])
    for i, idea in enumerate(ideas, 1):
        with st.expander(f"Idea {i}"):
            st.markdown(idea)
            col1, col2 = st.columns(2)
            with col1:
                st.button(f"👍 Me gusta", key=f"like_{i}")
            with col2:
                st.button(f"📝 Detalles", key=f"details_{i}")

st.markdown("---")
st.markdown("### Creador de Ideas Personalizado")

context = st.text_area("Describe tu area de interes o problema:", height=100)

if st.button("Generar Ideas Personalizadas"):
    if context:
        st.info("Para generar ideas mas creativas con IA, configura una API key.")
        st.markdown("### Mientras tanto, aqui tienes algunas ideas relacionadas:")

        base_ideas = random.sample(idea_templates.get("negocio", []), 3)
        for i, idea in enumerate(base_ideas, 1):
            st.markdown(f"{i}. {idea}")

st.markdown("""
### Acerca de este Template

**Template 4: Idea Generator**

Generador de ideas predefinidas por categoria.
Funciona sin API key para inspiracion rapida.
""")
