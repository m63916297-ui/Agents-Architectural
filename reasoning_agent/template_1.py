"""
Reasoning Agent - Template 1: Logic Puzzles
Arquitectura: Chain-of-Thought
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Reasoning T1", page_icon="🧩")

st.title("🧩 Logic Puzzles")
st.markdown("**Arquitectura:** Chain-of-Thought | **Modo:** Puzzles Logicos")

st.markdown("---")

puzzles = {
    "1": {
        "title": "El lago y los nenufares",
        "problem": "Un nenufar duplica su tamano cada dia. En 30 dias cubre el lago. En que dia cubre la mitad?",
        "answer": "Dia 29. Si duplica su tamano cada dia y cubre todo el lago en 30 dias, entonces la mitad del lago estaria cubierta un dia antes, es decir, en el dia 29.",
        "reasoning": "Este es un problema clasico de crecimiento exponencial. Piensa al reves: si el dia 30 cubre el 100%, el dia 29 cubre el 50%.",
    },
    "2": {
        "title": "Las dos puertas",
        "problem": "Estas frente a dos puertas. Una lleva al libertad, otra a la muerte. Un guardia siempre miente, el otro siempre dice la verdad. Solo puedes hacer una pregunta. Que preguntas para encontrar la puerta correcta?",
        "answer": "Pregunta a cualquier guardia: 'Si le preguntara al otro guardia cual es la puerta correcta, que me diria?' Ambas puertas llevaran a la respuesta correcta porque el mentiroso imitara al honesto y viceversa.",
        "reasoning": "Esta es una paradoja de autorreferencia. Al preguntar sobre lo que diria el otro, ambos daran la respuesta incorrecta, asi que debes tomar la opuesta.",
    },
    "3": {
        "title": "Los 3 interruptores",
        "problem": "Hay 3 interruptores en una habitacion y una bombilla en otra. Solo puedes pasar una vez. Como descubres cual interruptor enciende la bombilla?",
        "answer": "Enciende el primer interruptor por 10 minutos, luego apaga y enciende el segundo. Entra a la otra habitacion: si la bombilla esta encendida, es el segundo; si esta apagada pero caliente, es el primero; si esta apagada y fria, es el tercero.",
        "reasoning": "La solucion usa la propiedad termica de la bombilla. Solo el primer interruptor calentara la bombilla si estuvo encendida.",
    },
}

selected = st.selectbox("Selecciona un puzzle:", [""] + list(puzzles.keys()))

if selected and selected in puzzles:
    puz = puzzles[selected]
    with st.expander(f"📖 {puz['title']}", expanded=True):
        st.markdown(f"### Problema:")
        st.info(puz["problem"])

        show_reasoning = st.checkbox("Mostrar razonamiento")
        show_answer = st.checkbox("Mostrar respuesta")

        if show_reasoning:
            st.markdown("### Razonamiento:")
            st.markdown(puz["reasoning"])

        if show_answer:
            st.markdown("### Respuesta:")
            st.success(puz["answer"])

st.markdown("---")
st.markdown("""
### Acerca de este Template

**Template 1: Logic Puzzles**

Resuelve puzzles logicos conChain-of-Thought.
""")
