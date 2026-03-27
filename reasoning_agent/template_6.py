"""
Reasoning Agent - Template 6: Syllogism Solver
Arquitectura: Chain-of-Thought
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Reasoning T6", page_icon="⚖️")

st.title("⚖️ Syllogism Solver")
st.markdown("**Arquitectura:** Chain-of-Thought | **Modo:** Logica Silogistica")

st.markdown("---")

syllogisms = {
    "1": {
        "premises": ["Todos los humanos son mortales", "Socrates es humano"],
        "conclusion": "Socrates es mortal",
        "valid": True,
        "reasoning": "Premisa 1: Todos los H son M. Premisa 2: Socrates es H. Por lo tanto, Socrates es M. Este es un silogismo categorico valido.",
    },
    "2": {
        "premises": ["Todos los perros son animales", "Ningun gato es perro"],
        "conclusion": "Ningun gato es animal",
        "valid": False,
        "reasoning": "Este silogismo es invalido. La conclusion no se sigue logicamente. Aunque todos los perros son animales, eso no implica nada sobre los gatos. Un silogismo correcto seria: Todos los perros son animales, Felix es un gato, por lo tanto Felix es un animal.",
    },
    "3": {
        "premises": [
            "Algunos desarrolladores usan Python",
            "Algunos que usan Python usan IA",
        ],
        "conclusion": "Algunos desarrolladores usan IA",
        "valid": False,
        "reasoning": "Este es un silogismo invalido. Las premisas no garantizan la conclusion porque podrian ser conjuntos diferentes de personas. Se necesita una premisa que conecte directamente los dos grupos.",
    },
}

st.markdown("### Ejemplos de Silogismos")

for key, syl in syllogisms.items():
    with st.expander(f"Silogismo #{key}"):
        st.markdown("#### Premisas:")
        for p in syl["premises"]:
            st.markdown(f"- {p}")
        st.markdown(f"#### Conclusion propuesta: {syl['conclusion']}")

        if st.button(f"Mostrar analisis #{key}"):
            if syl["valid"]:
                st.success("✅ Silogismo VALIDO")
            else:
                st.error("❌ Silogismo INVALIDO")
            st.markdown(f"**Razonamiento:** {syl['reasoning']}")

st.markdown("---")
st.markdown("### Crea tu propio Silogismo")

st.markdown("#### Premisa 1:")
p1 = st.text_input("Todos los ___ son ___")
st.markdown("#### Premisa 2:")
p2 = st.text_input("Todos los ___ son ___")
st.markdown("#### Conclusion propuesta:")
conclusion = st.text_input("Todos los ___ son ___")

if p1 and p2 and conclusion:
    st.markdown("---")
    st.markdown("### Analisis")
    st.info(
        "Para verificar la validez, el termino medio debe aparecer en ambas premisas y conectar correctamente los terminos."
    )

    st.markdown("""
    **Reglas de validacion:**
    1. El termino medio debe estar en ambas premisas
    2. No se puede concluir de dos premisas negativas
    3. La conclusion no puede ser mas especifica que las premisas
    """)

st.markdown("""
### Acerca de este Template

**Template 6: Syllogism Solver**

Resuelve y crea silogismos logicos.
""")
