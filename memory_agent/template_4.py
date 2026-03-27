"""
Memory Agent - Template 4: Personal Wiki
Arquitectura: Conversation Memory
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_page_config(title="Memory T4", page_icon="📖")

st.title("📖 Personal Wiki")
st.markdown("**Arquitectura:** Conversation Memory | **Modo:** Wiki Personal")

st.markdown("---")

if 'wiki' not in st.session_state:
    st.session_state.wiki = {}

st.markdown("### Crear Articulo")

title = st.text_input("Titulo del articulo:")
content = st.text_area("Contenido:", height=200)

if st.button("Guardar articulo") and title and content:
    st.session_state.wiki[title] = content
    st.success("Articulo guardado!")

st.markdown("---")
st.markdown("### Articulos Guardados")

search = st.text_input("Buscar articulos:")

for article_title, article_content in st.session_state.wiki.items():
    if search.lower() in article_title.lower() or search.lower() in article_content.lower():
        with st.expander(f"📄 {article_title}"):
            st.markdown(article_content)
            if st.button(f"Eliminar: {article_title}"):
                del st.session_state.wiki[article_title]
                st.rerun()

st.markdown(f"**Total articulos:** {len(st.session_state.wiki)}")

st.markdown("""
### Acerca de este Template

**Template 4: Personal Wiki**

Almacena y busca articulos personales.
""")
