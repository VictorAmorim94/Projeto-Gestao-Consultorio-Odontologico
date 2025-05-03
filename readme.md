# 📊 Gestão - Consultório Odontológico

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)
![Google Sheets API](https://img.shields.io/badge/Google%20Sheets-34A853?logo=googlesheets&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em%20Andamento-yellow)

---

Aplicativo web desenvolvido em **Streamlit** para gerenciar um consultório odontológico. O sistema permitirá:
- Cadastrar entradas e saídas de valores 
- Agendar Pacientes
- Verificar Estoque

---

## Funcionalidades

- Cadastro de lançamentos com:
  - Nome
  - CPF (com validação)
  - Entrada ou saída
  - Forma de pagamento
  - Valor
  - Data
  - E-mail
- Visualização dos lançamentos em formato de tabela
- Remoção de lançamentos com botão de lixeira 🗑️
- Integração com Google Sheets
- Validação e formatação automática de CPF

---

## Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [gspread](https://docs.gspread.org/)
- [Google Sheets API](https://developers.google.com/sheets/api)
- [python-dotenv](https://saurabh-kumar.com/python-dotenv/)

---

## 🛠️ Instalação

Clone o projeto e crie um ambiente virtual:

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
```

## 🔐 Variáveis de Ambiente
Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:
```bash
GOOGLE_SHEETS_CREDENTIALS_PATH=credentials.json
GOOGLE_SHEET_ID=seu_id_da_planilha_google_sheets
ABA_LIVRO_CAIXA=LivroCaixa
```
- O arquivo credentials.json é gerado ao configurar o acesso à Google Sheets API.

- Importante: Compartilhe sua planilha com o e-mail da conta de serviço (contido no credentials.json).

## ▶️ Executar o App
```bash
streamlit run app.py
```

Se estiver usando estrutura com múltiplas páginas, certifique-se de que os arquivos .py estão organizados corretamente na pasta pages/.

## 🧪 Para Testes 

Para testar, estou disponibilizando um arquivo livro_caixa_teste.xlsx gerado pela lib faker. 

## 📌 Status
Projeto em desenvolvimento com funcionalidades básicas já implementadas. Novos recursos planejados:

- Otimização do Livro Caixa:
    - Inserção de Operações de Entrada e Saída✅
    - Edição de Valores
    - Implementação com GCP
    - Dashboard Financeiro - PowerBI
- Paciente:
    - Criação de Pacientes
    - Inserção de Evolução de Pacientes
    - Inserção de Fotos de plano Odontológico
- Agenda:
    - Criação de agendamento(Criação, exclusão, edição)
    - Automação de Agendamento via API
- Verificar Estoque: Módulo para ser todo voltado a Inteligência artificial.
    - Enviar foto do Estoque
    - Calcular Estoque
    - Gerência de Estoque

