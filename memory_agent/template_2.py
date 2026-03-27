"""
Memory Agent - Template 2: User Profile
Arquitectura: Conversation Memory
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Memory T2", page_icon="👤")

st.title("👤 User Profile Memory")
st.markdown("**Arquitectura:** Conversation Memory | **Modo:** Perfil de Usuario")

st.markdown("---")

if "user_profile" not in st.session_state:
    st.session_state.user_profile = {"name": "", "preferences": [], "history": []}

st.markdown("### Informacion Personal")

name = st.text_input("Nombre:", value=st.session_state.user_profile.get("name", ""))
if name != st.session_state.user_profile.get("name", ""):
    st.session_state.user_profile["name"] = name
    st.session_state.user_profile["history"].append(f"Nombre actualizado a: {name}")

st.markdown("---")
st.markdown("### Preferencias")

preferences = st.multiselect(
    "Selecciona tus intereses:",
    [
        "Tecnologia",
        "Deportes",
        "Musica",
        "Viajes",
        "Cocina",
        "Arte",
        "Ciencia",
        "Negocios",
    ],
)

if st.button("Guardar preferencias"):
    st.session_state.user_profile["preferences"] = preferences
    st.session_state.user_profile["history"].append(
        f"Preferencias actualizadas: {', '.join(preferences)}"
    )
    st.success("Preferencias guardadas!")

st.markdown("---")
st.markdown("### Preferencias Actuales")
for pref in st.session_state.user_profile.get("preferences", []):
    st.markdown(f"- {pref}")

st.markdown("---")
st.markdown("### Historial de Cambios")

for item in st.session_state.user_profile.get("history", [])[-10:][::-1]:
    st.markdown(f"- {item}")

st.markdown("""
### Acerca de este Template

**Template 2: User Profile Memory**

Guarda y recuerda informacion del usuario.
""")
