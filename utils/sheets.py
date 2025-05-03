import gspread
from gspread_dataframe import set_with_dataframe, get_as_dataframe
import pandas as pd
import os

def conectar_planilha(nome_aba):
    gc = gspread.service_account(filename='D:\\app_consultorio\\data\\credentials.json')
    sh = gc.open("Livro Caixa Consultorio")  # Nome da planilha no Google Drive
    worksheet = sh.worksheet(nome_aba)
    return worksheet

def carregar_dados(nome_aba):
    ws = conectar_planilha(nome_aba)
    df = get_as_dataframe(ws, evaluate_formulas=True)
    df.dropna(how="all", inplace=True)  # Remove linhas totalmente vazias
    return df

def salvar_dados(nome_aba, df):
    ws = conectar_planilha(nome_aba)
    ws.clear()
    set_with_dataframe(ws, df)
