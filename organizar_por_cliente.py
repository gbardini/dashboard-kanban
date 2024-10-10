import pandas as pd
import streamlit as st
from utils import convert_to_date

st.set_page_config(layout='wide')

# Carregar o arquivo CSV
df = pd.read_csv('/app/data/file.csv', sep=';', encoding='ISO-8859-1')
print(df.columns)

# Converter a coluna "Data da última ação"
if 'Data da última ação' in df.columns:
    df['Data da última ação'] = convert_to_date(df['Data da última ação'])

# Agrupar os dados pela coluna "Cliente (Organização)"
client_groups = df.groupby("Cliente (Organização)")

# Criar o dashboard
st.title("Dashboard Kanban por Cliente")
st.markdown(f"Total de tickets: **{len(df)}**")  # Contador de registros

# Exibir os grupos de clientes
for client, group in client_groups:
    st.subheader(f"Cliente: {client}")

    # Armazenando o DataFrame do grupo
    formatted_group = group[['Número', 'Data da última ação', 'Assunto', 'Cliente (Organização)', 'Responsável', 'Status']].copy()

    # Convertendo 'Número' para string
    formatted_group['Número'] = formatted_group['Número'].astype(str)

    st.dataframe(formatted_group)