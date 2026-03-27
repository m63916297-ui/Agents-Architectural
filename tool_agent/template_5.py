"""
Tool Agent - Template 5: QR Generator
Arquitectura: ReAct (Tool Use)
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Tool T5", page_icon="📱")

st.title("📱 QR Code Generator")
st.markdown("**Arquitectura:** ReAct (Tool Use) | **Modo:** Generador de Codigos QR")

st.markdown("---")

st.markdown("### Generar Codigo QR")

content = st.text_area(
    "Contenido del QR:", height=100, placeholder="https://ejemplo.com"
)

qr_types = {
    "URL": "Enlace web",
    "Texto": "Texto plano",
    "WiFi": "Configuracion WiFi",
    "Email": "Correo electronico",
    "Telefono": "Numero telefonico",
}

qr_type = st.selectbox("Tipo de contenido:", list(qr_types.keys()))

if qr_type == "URL":
    sample = "https://www.ejemplo.com"
elif qr_type == "Texto":
    sample = "Hola, este es un mensaje de prueba"
elif qr_type == "WiFi":
    sample = "WIFI:T:WPA;S:MiRed;P:MiContrasena;;"
elif qr_type == "Email":
    sample = "mailto:correo@ejemplo.com"
else:
    sample = "tel:+1234567890"

if st.button("Generar QR"):
    if content or sample:
        display_content = content if content else sample

        st.success(f"### Codigo QR generado para:")
        st.code(
            display_content[:50] + "..."
            if len(display_content) > 50
            else display_content
        )

        st.markdown("""
        ```
        ┌─────────────────────────────┐
        │  ▓▓▓▓  ▓▓▓▓  ▓▓▓▓  ▓▓▓▓  │
        │  ▓▓▓▓        ▓▓▓▓        │
        │       ▓▓▓▓  ▓▓▓▓       ▓▓▓▓  │
        │  ▓▓▓▓        ▓▓▓▓  ▓▓▓▓  │
        │  ▓▓▓▓  ▓▓▓▓  ▓▓▓▓        │
        │             ▓▓▓▓            │
        │  ▓▓▓▓  ▓▓▓▓        ▓▓▓▓  │
        │       ▓▓▓▓  ▓▓▓▓  ▓▓▓▓       │
        │  ▓▓▓▓        ▓▓▓▓  ▓▓▓▓  │
        └─────────────────────────────┘
        ```
        """)

        st.info(
            "Nota: Para generar codigos QR reales, usa una libreria como 'qrcode' en Python."
        )

st.markdown("---")
st.markdown("### Usos comunes de QR")

uses = {
    "Restaurantes": "Menu digital",
    "Tienda": "支付 Links de pago",
    "Eventos": "Registro rapido",
    "Educacion": "Enlaces a recursos",
    "Negocios": "Informacion de contacto",
}

for use, desc in uses.items():
    st.markdown(f"- **{use}:** {desc}")

st.markdown("""
### Acerca de este Template

**Template 5: QR Code Generator**

Plantilla para generacion de codigos QR.
""")
