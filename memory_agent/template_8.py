"""
Memory Agent - Template 8: Contact Memory
Arquitectura: Conversation Memory
Sin API Key requerida
"""

import streamlit as st

st.set_page_config(page_title="Memory T8", page_icon="👥")

st.title("👥 Contact Memory")
st.markdown("**Arquitectura:** Conversation Memory | **Modo:** Memoria de Contactos")

st.markdown("---")

if "contacts" not in st.session_state:
    st.session_state.contacts = []

st.markdown("### Nuevo Contacto")

name = st.text_input("Nombre:")
email = st.text_input("Email:")
phone = st.text_input("Telefono:")
company = st.text_input("Empresa:")
notes = st.text_area("Notas:", height=80)

if st.button("Guardar contacto") and name:
    st.session_state.contacts.append(
        {
            "name": name,
            "email": email,
            "phone": phone,
            "company": company,
            "notes": notes,
        }
    )
    st.success("Contacto guardado!")

st.markdown("---")
st.markdown("### Buscar Contactos")

search = st.text_input("Buscar por nombre:")

for contact in st.session_state.contacts:
    if search.lower() in contact["name"].lower():
        with st.expander(f"👤 {contact['name']}"):
            if contact["email"]:
                st.markdown(f"**Email:** {contact['email']}")
            if contact["phone"]:
                st.markdown(f"**Telefono:** {contact['phone']}")
            if contact["company"]:
                st.markdown(f"**Empresa:** {contact['company']}")
            if contact["notes"]:
                st.markdown(f"**Notas:** {contact['notes']}")

            if st.button(f"Eliminar: {contact['name']}"):
                st.session_state.contacts.remove(contact)
                st.rerun()

st.markdown(f"**Total contactos:** {len(st.session_state.contacts)}")

st.markdown("""
### Acerca de este Template

**Template 8: Contact Memory**

Gestiona informacion de contactos.
""")
