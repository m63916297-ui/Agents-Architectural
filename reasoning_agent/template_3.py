"""
Reasoning Agent - Template 3: Decision Tree
Arquitectura: Chain-of-Thought
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Reasoning T3", page_icon="🌳")

st.title("🌳 Decision Tree Maker")
st.markdown("**Arquitectura:** Chain-of-Thought | **Modo:** Arbol de Decision")

st.markdown("---")

st.markdown("### Construye tu Arbol de Decision")

decision = st.text_input("Cual es tu decision principal?")

st.markdown("#### Opciones:")
options = []
for i in range(4):
    opt = st.text_input(f"Opcion {i + 1}:", key=f"opt_{i}")
    if opt:
        options.append(opt)

if decision and options:
    st.markdown(f"### Arbol de Decision: {decision}")

    for opt in options:
        with st.expander(f"**{opt}**"):
            pros = st.text_area(f"Pros de {opt}:", key=f"pros_{opt}")
            cons = st.text_area(f"Contras de {opt}:", key=f"cons_{opt}")

            if pros and cons:
                pro_list = [p.strip() for p in pros.split("\n") if p.strip()]
                con_list = [c.strip() for c in cons.split("\n") if c.strip()]

                st.markdown(f"**Pros ({len(pro_list)}):** {len(pro_list)}")
                st.markdown(f"**Contras ({len(con_list)}):** {len(con_list)}")

                if len(pro_list) > len(con_list):
                    st.success(f"✅ {opt} parece ser la mejor opcion")
                elif len(pro_list) < len(con_list):
                    st.warning(f"⚠️ {opt} tiene mas contras que pros")
                else:
                    st.info(f"ℹ️ {opt} esta equilibrado")

st.markdown("---")
st.markdown("### Matriz de Decision")

if options:
    st.markdown("#### Pros vs Contras")
    col = st.columns(len(options) + 1)
    with col[0]:
        st.markdown("**Criterio**")
        st.markdown("Pros")
        st.markdown("Contras")
        st.markdown("**Total**")

    for i, opt in enumerate(options):
        with col[i + 1]:
            st.markdown(f"**{opt[:10]}...**")
            st.markdown(f"{len(opt)}")
            st.markdown(f"{len(opt) // 2}")
            score = len(opt) - len(opt) // 2
            if score > 0:
                st.markdown(f"+{score}")
            else:
                st.markdown(f"{score}")

st.markdown("""
### Acerca de este Template

**Template 3: Decision Tree Maker**

Ayuda a tomar decisiones con un enfoque estructurado.
""")
