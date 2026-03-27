"""
Reasoning Agent - Template 10: Step Analyzer
Arquitectura: Chain-of-Thought
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Reasoning T10", page_icon="📋")

st.title("📋 Step-by-Step Analyzer")
st.markdown("**Arquitectura:** Chain-of-Thought | **Modo:** Analisis Paso a Paso")

st.markdown("---")

st.markdown("### Ingresa un Problema o Proceso")

process = st.text_area("Describe el problema o proceso:", height=100)

st.markdown("### Selecciona el Tipo de Analisis")

analysis_type = st.radio(
    "Tipo de analisis:", ["Causa raiz", "Proceso", "Decision", "Aprendizaje"]
)

if process:
    if analysis_type == "Causa raiz":
        st.markdown("""
        ### Analisis de Causa Raiz - 5 Porques
        
        Pregunta "Por que?" repetidamente para llegar a la causa raiz.
        """)

        why_count = st.slider("Cuantas veces preguntar 'Por que'?", 3, 7, 5)

        causes = []
        for i in range(why_count):
            cause = st.text_input(f"Porque #{i + 1}:", key=f"why_{i}")
            if cause:
                causes.append(cause)

        if causes:
            st.markdown("---")
            st.markdown("### Cadena de Causas")
            for i, cause in enumerate(causes):
                st.markdown(f"**Por que #{i + 1}:** {cause}")

            st.success(f"✅ Causa raiz identificada: {causes[-1]}")

    elif analysis_type == "Proceso":
        st.markdown("""
        ### Analisis de Proceso
        
        Descompone el proceso en pasos secuenciales.
        """)

        steps = []
        for i in range(8):
            step = st.text_input(f"Paso {i + 1}:", key=f"step_{i}")
            if step:
                steps.append(step)

        if steps:
            st.markdown("---")
            st.markdown("### Proceso Secuencial")
            for i, step in enumerate(steps, 1):
                col1, col2 = st.columns([1, 4])
                with col1:
                    st.markdown(f"**{i}.**")
                with col2:
                    st.markdown(step)
                if i < len(steps):
                    st.markdown("↓")

    elif analysis_type == "Decision":
        st.markdown("""
        ### Analisis de Decision
        
        Evalua pros, contras y consecuencias.
        """)

        decision = st.text_input("Decision:")
        pros = st.text_area("Pros (uno por linea):").split("\n")
        cons = st.text_area("Contras (uno por linea):").split("\n")

        if pros and cons:
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("✅ **Pros**")
                for pro in pros:
                    if pro.strip():
                        st.markdown(f"- {pro}")
            with col2:
                st.markdown("❌ **Contras**")
                for con in cons:
                    if con.strip():
                        st.markdown(f"- {con}")

            pro_count = len([p for p in pros if p.strip()])
            con_count = len([c for c in cons if c.strip()])

            if pro_count > con_count:
                st.success("✅ La decision parece favorable")
            elif con_count > pro_count:
                st.warning("⚠️ Revisa los contras antes de decidir")
            else:
                st.info("ℹ️ La decision esta equilibrada")

    else:  # Aprendizaje
        st.markdown("""
        ### Analisis de Aprendizaje
        
        Identifica que funciono, que no, y que aprendiste.
        """)

        col1, col2, col3 = st.columns(3)

        with col1:
            worked = st.text_area("Que funciono bien?").split("\n")
            st.markdown("✅ **Fucioneso**")
            for w in worked:
                if w.strip():
                    st.markdown(f"- {w}")

        with col2:
            failed = st.text_area("Que no funciono?").split("\n")
            st.markdown("❌ **No funciono**")
            for f in failed:
                if f.strip():
                    st.markdown(f"- {f}")

        with col3:
            learned = st.text_area("Que aprendiste?").split("\n")
            st.markdown("📚 **Aprendizajes**")
            for l in learned:
                if l.strip():
                    st.markdown(f"- {l}")

st.markdown("""
### Acerca de este Template

**Template 10: Step-by-Step Analyzer**

Analiza problemas desde multiples perspectivas.
""")
