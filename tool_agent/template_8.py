"""
Tool Agent - Template 8: Text Analyzer
Arquitectura: ReAct (Tool Use)
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Tool T8", page_icon="📊")

st.title("📊 Text Analyzer Tool")
st.markdown("**Arquitectura:** ReAct (Tool Use) | **Modo:** Analizador de Texto")

st.markdown("---")

text = st.text_area("Texto a analizar:", height=150)

if text:
    st.markdown("---")
    st.markdown("### Estadisticas Basicas")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Caracteres", len(text))
    col2.metric("Palabras", len(text.split()))
    col3.metric("Lineas", len(text.split("\n")))
    col4.metric("Caracteres (sin espacios)", len(text.replace(" ", "")))

    st.markdown("---")
    st.markdown("### Analisis Detallado")

    words = text.split()
    vowels = sum(1 for c in text.lower() if c in "aeiouáéíóú")
    consonants = sum(1 for c in text.lower() if c.isalpha() and c not in "aeiouáéíóú")

    col1, col2, col3 = st.columns(3)
    col1.metric("Vocales", vowels)
    col2.metric("Consonantes", consonants)
    col3.metric("Espacios", text.count(" "))

    st.markdown("---")
    st.markdown("### Frecuencia de Letras")

    from collections import Counter

    letters = [c.lower() for c in text if c.isalpha()]
    freq = Counter(letters)

    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:10]

    for letter, count in sorted_freq:
        percentage = (count / len(letters) * 100) if letters else 0
        st.progress(percentage / 100 * 5)
        st.markdown(f"**{letter.upper()}:** {count} ({percentage:.1f}%)")

    st.markdown("---")
    st.markdown("### Resumen de Palabras")

    word_freq = Counter(words)
    for word, count in word_freq.most_common(10):
        st.markdown(f"- {word}: {count}")

st.markdown("""
### Acerca de este Template

**Template 8: Text Analyzer Tool**

Analiza texto y genera estadisticas detalladas.
""")
