import gspread
from gspread_dataframe import set_with_dataframe, get_as_dataframe
import pandas as pd
from dotenv import load_dotenv
import os
load_dotenv()

def conectar_planilha(nome_aba):
    gc = gspread.service_account(filename=os.getenv("GOOGLE_SHEETS_CREDENTIALS_PATH"))
    sh = gc.open(os.getenv("NOME_SHEETS"))  #Nome Planilha google Drive
    worksheet = sh.worksheet(nome_aba)
    return worksheet

def carregar_dados(nome_aba):
    ws = conectar_planilha(nome_aba)
    df = get_as_dataframe(ws, evaluate_formulas=True)
    df.dropna(how="all", inplace=True)  
    return df

def salvar_dados(nome_aba, df):
    ws = conectar_planilha(nome_aba)
    ws.clear()
    set_with_dataframe(ws, df)
