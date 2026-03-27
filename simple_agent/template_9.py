"""
Simple Agent - Template 9: Notes/Flashcards
Arquitectura: Single-Agent
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Simple Agent T9", page_icon="📚")

st.title("📚 Notes & Flashcards")
st.markdown("**Arquitectura:** Single-Agent | **Modo:** Sistema de Notas")

st.markdown("---")

if "notes" not in st.session_state:
    st.session_state.notes = []

if "flashcards" not in st.session_state:
    st.session_state.flashcards = []

tab1, tab2 = st.tabs(["Notas", "Flashcards"])

with tab1:
    st.markdown("### Nueva Nota")
    note_title = st.text_input("Titulo:")
    note_content = st.text_area("Contenido:", height=150)
    note_category = st.selectbox(
        "Categoria:", ["General", "Importante", "Trabajo", "Personal"]
    )

    if st.button("💾 Guardar Nota"):
        if note_title and note_content:
            st.session_state.notes.append(
                {
                    "title": note_title,
                    "content": note_content,
                    "category": note_category,
                }
            )
            st.success("Nota guardada!")

    st.markdown("### Mis Notas")
    search = st.text_input("Buscar notas:")

    for note in st.session_state.notes[::-1]:
        if (
            search.lower() in note["title"].lower()
            or search.lower() in note["content"].lower()
        ):
            with st.expander(f"📝 {note['title']} ({note['category']})"):
                st.markdown(note["content"])
                if st.button(f"Eliminar", key=f"del_note_{note['title']}"):
                    st.session_state.notes.remove(note)
                    st.rerun()

with tab2:
    st.markdown("### Nueva Flashcard")
    fc_question = st.text_input("Pregunta:")
    fc_answer = st.text_area("Respuesta:", height=100)
    fc_topic = st.selectbox(
        "Tema:", ["General", "Ciencia", "Historia", "Matematicas", "Programacion"]
    )

    if st.button("➕ Crear Flashcard"):
        if fc_question and fc_answer:
            st.session_state.flashcards.append(
                {
                    "question": fc_question,
                    "answer": fc_answer,
                    "topic": fc_topic,
                    "known": False,
                }
            )
            st.success("Flashcard creada!")

    st.markdown("### Practicar")

    topic_filter = st.selectbox(
        "Filtrar por tema:",
        ["Todos"] + ["General", "Ciencia", "Historia", "Matematicas", "Programacion"],
    )

    filtered_cards = [
        fc
        for fc in st.session_state.flashcards
        if topic_filter == "Todos" or fc["topic"] == topic_filter
    ]

    if filtered_cards:
        card = random.choice(filtered_cards) if filtered_cards else None

        if card:
            with st.container():
                st.markdown(f"**Tema:** {card['topic']}")
                st.markdown(f"**Pregunta:** {card['question']}")

                if st.button("Mostrar Respuesta"):
                    st.success(f"**Respuesta:** {card['answer']}")

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("✅ La se", use_container_width=True):
                        card["known"] = True
                        st.rerun()
                with col2:
                    if st.button("❌ Necesito practicar", use_container_width=True):
                        card["known"] = False
                        st.rerun()
    else:
        st.info("No hay flashcards. Crea una para practicar!")

st.markdown("---")
st.markdown(
    f"**Total Notas:** {len(st.session_state.notes)} | **Total Flashcards:** {len(st.session_state.flashcards)}"
)

st.markdown("""
### Acerca de este Template

**Template 9: Notes & Flashcards**

Sistema de gestion de notas y tarjetas de estudio.
""")
