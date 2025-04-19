import requests
from pprint import pprint
import pandas as pd
import streamlit as st

st.title("Cotações de Moedas")

url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
puxar_cotacoes = requests.get(url=url)
mostrar_cotacoes = puxar_cotacoes.json()

#print(puxar_cotacoes)
#pprint(mostrar_cotacoes)-,

cotacao_dolar = mostrar_cotacoes["USDBRL"]["bid"]
cotacao_euro = mostrar_cotacoes["EURBRL"]["bid"]
cotacao_btc = mostrar_cotacoes["BTCBRL"]["bid"]

#print(f'A cotação atual do dólar é: {cotacao_dolar}')
#print(f'A cotação atual do euro é: {cotacao_euro}')
#print(f'A cotação atual do btc é: {cotacao_btc}')

cotacoes_tabela = {

    "Moeda": ["Dólar", "Euro", "BTC"],
    "Cotação_BRL": [cotacao_dolar, cotacao_euro, cotacao_btc]

}
df = pd.DataFrame(cotacoes_tabela)

#exibir tabela
print(df)

#mostrando no app
st.dataframe(df)

#Salvando em .CSV se for necessário:
#df.to_csv("cotacoes.csv", index=False, sep=";", decimal=",")
#print("Arquivo gerado com sucesso")

# o arquivo deve ser rodado como streamlit run nome_do_arquivo.py