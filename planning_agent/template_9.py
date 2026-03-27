"""
Planning Agent - Template 9: Budget Planner
Arquitectura: Plan-and-Solve
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Planning T9", page_icon="💰")

st.title("💰 Budget Planner")
st.markdown("**Arquitectura:** Plan-and-Solve | **Modo:** Planificador de Presupuesto")

st.markdown("---")

if "budget" not in st.session_state:
    st.session_state.budget = {"income": 0, "expenses": []}

st.markdown("### Ingresos")

income = st.number_input("Ingreso mensual:", value=0.0, key="income_input")

if st.button("Actualizar Ingreso"):
    st.session_state.budget["income"] = income

st.markdown("---")
st.markdown("### Gastos")

expense_name = st.text_input("Nombre del gasto:")
expense_amount = st.number_input("Monto:", value=0.0)
expense_category = st.selectbox(
    "Categoria:",
    [
        "Vivienda",
        "Alimentacion",
        "Transporte",
        "Salud",
        "Entretenimiento",
        "Educacion",
        "Ahorro",
        "Otros",
    ],
)

if st.button("Agregar Gasto") and expense_name and expense_amount > 0:
    st.session_state.budget["expenses"].append(
        {"name": expense_name, "amount": expense_amount, "category": expense_category}
    )

st.markdown("---")
st.markdown("### Resumen")

total_expenses = sum(e["amount"] for e in st.session_state.budget["expenses"])
balance = st.session_state.budget["income"] - total_expenses

col1, col2, col3 = st.columns(3)
col1.metric("Ingresos", f"${st.session_state.budget['income']:,.2f}")
col2.metric("Gastos", f"${total_expenses:,.2f}")
col3.metric(
    "Balance",
    f"${balance:,.2f}",
    delta=f"{'+' if balance > 0 else ''}{balance / st.session_state.budget['income'] * 100:.1f}%"
    if st.session_state.budget["income"] > 0
    else None,
)

st.markdown("---")
st.markdown("### Gastos por Categoria")

categories = {}
for expense in st.session_state.budget["expenses"]:
    cat = expense["category"]
    categories[cat] = categories.get(cat, 0) + expense["amount"]

for cat, amount in sorted(categories.items(), key=lambda x: x[1], reverse=True):
    percentage = (amount / total_expenses * 100) if total_expenses > 0 else 0
    st.progress(percentage / 100)
    st.markdown(f"**{cat}:** ${amount:,.2f} ({percentage:.1f}%)")

st.markdown("---")
st.markdown("### Lista de Gastos")

for i, expense in enumerate(st.session_state.budget["expenses"]):
    with st.expander(f"{expense['name']} - ${expense['amount']:,.2f}"):
        st.markdown(f"Categoria: {expense['category']}")
        if st.button("Eliminar", key=f"del_exp_{i}"):
            st.session_state.budget["expenses"].pop(i)
            st.rerun()

st.markdown("""
### Acerca de este Template

**Template 9: Budget Planner**

Controla ingresos y gastos mensuales.
""")
