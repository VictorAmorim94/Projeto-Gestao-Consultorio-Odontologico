import streamlit as st
import pandas as pd
from datetime import datetime
from utils.sheets import carregar_dados, salvar_dados
from utils.validators import validar_cpf
import os

def formatar_cpf(cpf):
    cpf = str(cpf).zfill(11)
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

# Interface do usuário
st.title("📒 Livro Caixa")

st.subheader("Adicionar Lançamento")

with st.form("form_lancamento"):
    nome = st.text_input("Nome")
    cpf = st.text_input("CPF")
    tipo = st.selectbox("Operação", ["Entrada", "Saída"])
    forma_pagamento = st.selectbox("Forma de Pagamento", ["Dinheiro", "Cartão", "PIX", "Outros"])
    valor = st.number_input("Valor (R$)", min_value=0.0, format="%.2f")
    data = st.date_input("Data", value=datetime.today())
    email = st.text_input("Email")
    
    submitted = st.form_submit_button("Adicionar")

    if submitted:
        novo_lancamento = pd.DataFrame([{
            "Nome": nome,
            "CPF": str(cpf),
            "Operacao": tipo,
            "Forma de Pagamento": forma_pagamento,
            "Valor": valor,
            "Data": data,
            "Email": email
        }])

        df_existente = carregar_dados("LivroCaixa")
        df_atualizado = pd.concat([df_existente, novo_lancamento], ignore_index=True)
        salvar_dados("LivroCaixa", df_atualizado)

        st.success("✅ Lançamento adicionado com sucesso!")

st.subheader("📊 Lançamentos Registrados")

df = carregar_dados("LivroCaixa") 

if df.empty:
    st.info("Nenhum lançamento registrado ainda.")
else:
    df = df.reset_index(drop=True)
    header_cols = st.columns([4, 2, 2, 2, 2, 2, 3, 1])
    headers = ["Nome", "CPF", "Tipo", "Forma Pgto", "Valor", "Data", "Email"]

    for col, name in zip(header_cols, headers):
        col.markdown(f"**{name}**")

    for i, row in df.iterrows():
        cols = st.columns([4, 2, 2, 2, 2, 2, 3, 1])
        cols[0].markdown(row["Nome"])
        cols[1].markdown(row["CPF"])
        cols[2].markdown(row["Operacao"])
        cols[3].markdown(row["Forma de Pagamento"])
        cols[4].markdown(f"R$ {row['Valor']:.2f}")
        cols[5].markdown(pd.to_datetime(row["Data"]).strftime("%d/%m/%Y"))
        cols[6].markdown(row["Email"])

        if cols[7].button("🗑️", key=f"del_{i}"):
            df = df.drop(i).reset_index(drop=True)
            salvar_dados("LivroCaixa", df)
            st.success(f"Lançamento de {row['Nome']} removido com sucesso!")
            st.rerun()