"""
Simple Agent - Template 8: Password Generator
Arquitectura: Single-Agent
Sin API Key requerida
"""

import streamlit as st
import random
import string

st.set_page_config(page_title="Simple Agent T8", page_icon="🔐")

st.title("🔐 Password Generator")
st.markdown("**Arquitectura:** Single-Agent | **Modo:** Generador de Contrasenas")

st.markdown("---")


def generate_password(length, use_upper, use_lower, use_digits, use_special):
    chars = ""
    if use_upper:
        chars += string.ascii_uppercase
    if use_lower:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation

    if not chars:
        chars = string.ascii_letters + string.digits

    return "".join(random.choice(chars) for _ in range(length))


def check_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c in string.ascii_uppercase for c in password):
        score += 1
    if any(c in string.ascii_lowercase for c in password):
        score += 1
    if any(c in string.digits for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Débil", "🔴"
    elif score <= 4:
        return "Media", "🟡"
    else:
        return "Fuerte", "🟢"


col1, col2 = st.columns(2)

with col1:
    st.markdown("### Configuracion")
    length = st.slider("Longitud:", 4, 32, 16)
    use_upper = st.checkbox("Mayusculas (A-Z)", value=True)
    use_lower = st.checkbox("Minusculas (a-z)", value=True)
    use_digits = st.checkbox("Numeros (0-9)", value=True)
    use_special = st.checkbox("Especiales (!@#$)", value=True)

with col2:
    st.markdown("### Contrasena Generada")

    if st.button("🔄 Generar Nueva", use_container_width=True):
        password = generate_password(
            length, use_upper, use_lower, use_digits, use_special
        )
        strength, icon = check_strength(password)
        st.session_state.current_password = password
        st.session_state.password_strength = strength
        st.session_state.strength_icon = icon

    if "current_password" in st.session_state:
        st.code(st.session_state.current_password, language=None)
        st.markdown(
            f"**Fortaleza:** {st.session_state.strength_icon} {st.session_state.password_strength}"
        )

        col_a, col_b = st.columns(2)
        with col_a:
            st.button("📋 Copiar")
        with col_b:
            st.button("🔄 Nueva")

st.markdown("---")
st.markdown("### Historial de Contrasenas")

if "password_history" not in st.session_state:
    st.session_state.password_history = []

if "current_password" in st.session_state:
    if st.button("Guardar en Historial"):
        st.session_state.password_history.append(
            {
                "password": st.session_state.current_password,
                "strength": st.session_state.password_strength,
                "length": len(st.session_state.current_password),
            }
        )

for i, item in enumerate(st.session_state.password_history[-5:][::-1]):
    with st.expander(f"Contrasena {i + 1}"):
        st.code(item["password"])
        st.markdown(f"Longitud: {item['length']} | Fortaleza: {item['strength']}")

st.markdown("---")
st.markdown("""
### Acerca de este Template

**Template 8: Password Generator**

Generador seguro de contrasenas con verificador de fortaleza.
""")
