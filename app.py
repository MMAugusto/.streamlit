import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Criando um cabeçalho com texto
st.title("Análise de Dados de Veículos")
st.header("Este é um aplicativo simples para análise de dados de veículos.")

# Carregando os dados
@st.cache
def load_data():
    data = pd.read_csv("vehicles.csv")
    return data

data = load_data()

# Botões para selecionar o tipo de gráfico
opcao_grafico = st.radio("Selecione o tipo de gráfico:", ("Histograma", "Gráfico de Dispersão"))

if opcao_grafico == "Histograma":
    # Criando um histograma
    st.subheader("Histograma da Distribuição de Preços dos Veículos")
    plt.figure(figsize=(8, 6))
    sns.histplot(data['price'], bins=20, kde=True)
    plt.xlabel('Preço')
    plt.ylabel('Contagem')
    plt.title('Distribuição de Preços')
    st.pyplot()

elif opcao_grafico == "Gráfico de Dispersão":
    # Criando um gráfico de dispersão
    st.subheader("Gráfico de Dispersão: Preço vs. Ano do Modelo")
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=data, x='model_year', y='price', hue='condition')
    plt.xlabel('Ano do Modelo')
    plt.ylabel('Preço')
    plt.title('Preço vs. Ano do Modelo')
    plt.legend(title='Condição')
    st.pyplot()

# Adicionando um botão para exportar os dados
if st.button("Exportar Dados"):
    data.to_csv("dados_exportados.csv", index=False)
    st.success("Os dados foram exportados com sucesso!")