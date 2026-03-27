"""
Reasoning Agent - Template 7: Problem Decomposition
Arquitectura: Chain-of-Thought
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Reasoning T7", page_icon="🧩")

st.title("🧩 Problem Decomposer")
st.markdown(
    "**Arquitectura:** Chain-of-Thought | **Modo:** Descomposicion de Problemas"
)

st.markdown("---")

st.markdown("### Describe tu Problema")

problem = st.text_area("Cual es el problema que quieres resolver?", height=100)

if problem:
    st.markdown("---")
    st.markdown("### Descomposicion del Problema")

    st.markdown("""
    1. **Entender el problema**
       - Cual es el objetivo final?
       - Cuales son las restricciones?
       - Cuales son los recursos disponibles?
    
    2. **Identificar subproblemas**
       - Divide en partes mas pequenas
       - Identifica dependencias
       - Establece prioridades
    
    3. **Analizar subproblemas**
       - Para cada subproblema:
         - Que informacion necesitas?
         - Que herramientas tienes?
         - Que habilidades requieres?
    
    4. **Planificar solucion**
       - Ordenar subproblemas
       - Establecer timeline
       - Asignar recursos
    """)

    st.markdown("---")
    st.markdown("### Subproblemas Identificados")

    num_subproblems = st.slider("Cuantos subproblemas tiene?", 2, 8, 4)

    subproblems = []
    for i in range(num_subproblems):
        sp = st.text_input(f"Subproblema {i + 1}:", key=f"sp_{i}")
        if sp:
            subproblems.append(sp)

    if subproblems:
        st.markdown("#### Plan de Accion:")
        for i, sp in enumerate(subproblems, 1):
            with st.expander(f"Paso {i}: {sp}"):
                st.markdown("**Acciones necesarias:**")
                st.markdown(f"- Investigar {sp}")
                st.markdown(f"- Definir alcance")
                st.markdown(f"- Ejecutar")
                st.markdown(f"- Verificar resultado")

st.markdown("""
### Acerca de este Template

**Template 7: Problem Decomposer**

Descompone problemas complejos en partes manejables.
""")
