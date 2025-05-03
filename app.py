import streamlit as st

st.set_page_config(page_title="Consultório Odontológico", layout="wide")

st.title("🦷 Consultório Odontológico")
st.subheader("Bem-vindo(a) ao sistema de gestão clínica!")

st.markdown("""
Escolha uma página no menu lateral para começar:
- 📋 Cadastro de Pacientes
- 📆 Agenda de Atendimentos
- 💸 Controle Financeiro
""")
