"""
Tool Agent - Template 6: Color Picker
Arquitectura: ReAct (Tool Use)
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Tool T6", page_icon="🎨")

st.title("🎨 Color Picker & Converter")
st.markdown("**Arquitectura:** ReAct (Tool Use) | **Modo:** Selector de Colores")

st.markdown("---")

colors = {
    "Rojo": "#FF0000",
    "Azul": "#0000FF",
    "Verde": "#00FF00",
    "Amarillo": "#FFFF00",
    "Naranja": "#FF8800",
    "Morado": "#8800FF",
    "Rosa": "#FF0088",
    "Negro": "#000000",
    "Blanco": "#FFFFFF",
    "Gris": "#888888",
}

st.markdown("### Seleccionar Color")

color_name = st.selectbox("Color:", [""] + list(colors.keys()))

if color_name:
    hex_code = colors[color_name]

    col1, col2, col3 = st.columns(3)
    col1.markdown("### ")
    col1.markdown(
        f'<div style="background-color:{hex_code};width:100px;height:100px;border:1px solid black;"></div>',
        unsafe_allow_html=True,
    )

    col2.markdown("### ")
    col2.success(f"**HEX:** {hex_code}")

    r = int(hex_code[1:3], 16)
    g = int(hex_code[3:5], 16)
    b = int(hex_code[5:7], 16)
    col3.success(f"**RGB:** ({r}, {g}, {b})")

st.markdown("---")
st.markdown("### Conversor de Color")

st.markdown("#### HEX a RGB")
hex_input = st.text_input("Codigo HEX:", value="#FF5733")

if st.button("Convertir"):
    if hex_input.startswith("#") and len(hex_input) == 7:
        try:
            r = int(hex_input[1:3], 16)
            g = int(hex_input[3:5], 16)
            b = int(hex_input[5:7], 16)
            st.success(f"**RGB:** ({r}, {g}, {b})")

            st.markdown(
                f'<div style="background-color:{hex_input};width:200px;height:50px;"></div>',
                unsafe_allow_html=True,
            )
        except:
            st.error("Codigo HEX invalido")
    else:
        st.warning("Usa formato: #RRGGBB")

st.markdown("---")
st.markdown("### Paletas de Colores")

palettes = {
    "Primarios": [("Rojo", "#FF0000"), ("Azul", "#0000FF"), ("Amarillo", "#FFFF00")],
    " Secundarios": [
        ("Naranja", "#FF8800"),
        ("Verde", "#00FF00"),
        ("Morado", "#8800FF"),
    ],
    "Neutros": [("Negro", "#000000"), ("Gris", "#888888"), ("Blanco", "#FFFFFF")],
}

for palette, cols in palettes.items():
    st.markdown(f"#### {palette}")
    cols_row = st.columns(3)
    for i, (name, hex_val) in enumerate(cols):
        with cols_row[i]:
            st.markdown(
                f'<div style="background-color:{hex_val};width:80px;height:40px;border:1px solid black;"></div>',
                unsafe_allow_html=True,
            )
            st.caption(name)

st.markdown("""
### Acerca de este Template

**Template 6: Color Picker**

Selecciona y convierte colores.
""")
