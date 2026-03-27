"""
Simple Agent - Template 6: Calculator/Converter
Arquitectura: Single-Agent
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Simple Agent T6", page_icon="🧮")

st.title("🧮 Calculator & Converter")
st.markdown("**Arquitectura:** Single-Agent | **Modo:** Calculadora/Convertidor")

st.markdown("---")

tab1, tab2, tab3, tab4 = st.tabs(
    ["Calculadora", "Conversiones", "Porcentajes", "Estadisticas"]
)

with tab1:
    st.markdown("### Calculadora Basica")
    col1, col2, col3, col4 = st.columns(4)

    if "calc_result" not in st.session_state:
        st.session_state.calc_result = "0"

    def calc_click(val):
        if st.session_state.calc_result == "0" and val not in ["+", "-", "*", "/"]:
            st.session_state.calc_result = val
        else:
            st.session_state.calc_result += val

    def calc_clear():
        st.session_state.calc_result = "0"

    def calc_eval():
        try:
            st.session_state.calc_result = str(eval(st.session_state.calc_result))
        except:
            st.session_state.calc_result = "Error"

    st.text_input(
        "Resultado:", st.session_state.calc_result, key="display", disabled=True
    )

    cols = [
        ["7", "8", "9", "+"],
        ["4", "5", "6", "-"],
        ["1", "2", "3", "*"],
        ["C", "0", "=", "/"],
    ]

    for row in cols:
        cols_row = st.columns(4)
        for i, val in enumerate(row):
            if cols_row[i].button(val, use_container_width=True):
                if val == "C":
                    calc_clear()
                elif val == "=":
                    calc_eval()
                else:
                    calc_click(val)
                st.rerun()

with tab2:
    st.markdown("### Conversiones")

    conversion_type = st.selectbox(
        "Tipo:", ["Longitud", "Peso", "Temperatura", "Tiempo"]
    )

    if conversion_type == "Longitud":
        val = st.number_input("Valor:", value=1.0)
        from_unit = st.selectbox(
            "De:", ["Metros", "Centimetros", "Kilometros", "Pies", "Pulgadas", "Millas"]
        )
        to_unit = st.selectbox(
            "A:", ["Metros", "Centimetros", "Kilometros", "Pies", "Pulgadas", "Millas"]
        )

        conversions = {
            ("Metros", "Centimetros"): 100,
            ("Metros", "Kilometros"): 0.001,
            ("Metros", "Pies"): 3.28084,
            ("Centimetros", "Metros"): 0.01,
            ("Kilometros", "Metros"): 1000,
            ("Pies", "Metros"): 0.3048,
            ("Pulgadas", "Centimetros"): 2.54,
            ("Millas", "Kilometros"): 1.60934,
        }

        if from_unit == to_unit:
            result = val
        elif (from_unit, to_unit) in conversions:
            result = val * conversions[(from_unit, to_unit)]
        elif (to_unit, from_unit) in conversions:
            result = val / conversions[(to_unit, from_unit)]
        else:
            result = "Conversion no disponible"

        st.success(f"{val} {from_unit} = {result} {to_unit}")

    elif conversion_type == "Temperatura":
        val = st.number_input("Valor:")
        unit = st.selectbox("Unidad:", ["Celsius", "Fahrenheit", "Kelvin"])

        if unit == "Celsius":
            f = val * 9 / 5 + 32
            k = val + 273.15
        elif unit == "Fahrenheit":
            c = (val - 32) * 5 / 9
            k = c + 273.15
        else:
            c = val - 273.15
            f = c * 9 / 5 + 32

        st.info(
            f"Fahrenheit: {f:.2f}°F | Kelvin: {k:.2f}K"
            if unit == "Celsius"
            else f"Celsius: {c:.2f}°C | Kelvin: {k:.2f}K"
        )

with tab3:
    st.markdown("### Calculos de Porcentaje")
    pct_val = st.number_input("Valor:", value=100.0)
    pct_rate = st.number_input("Porcentaje:", value=10.0)

    col1, col2 = st.columns(2)
    with col1:
        st.metric("X% de valor", pct_val * pct_rate / 100)
    with col2:
        st.metric("Valor + X%", pct_val * (1 + pct_rate / 100))

    st.markdown("---")
    original = st.number_input("Original:", value=80.0)
    nuevo = st.number_input("Nuevo:", value=100.0)
    cambio = ((nuevo - original) / original * 100) if original != 0 else 0
    st.metric("Cambio porcentual", f"{cambio:.2f}%")

with tab4:
    st.markdown("### Estadisticas Basicas")
    numbers = st.text_input("Numeros (separados por coma):", "1,2,3,4,5")

    if numbers:
        try:
            nums = [float(n.strip()) for n in numbers.split(",") if n.strip()]
            if nums:
                st.metric("Cantidad", len(nums))
                st.metric("Suma", sum(nums))
                st.metric("Promedio", sum(nums) / len(nums))
                st.metric("Minimo", min(nums))
                st.metric("Maximo", max(nums))
        except:
            st.error("Ingresa numeros validos separados por coma")

st.markdown("""
### Acerca de este Template

**Template 6: Calculator & Converter**

Herramientas de calculo y conversion de unidades.
""")
