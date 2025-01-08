import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1 - Importando os Dados
data = pd.read_csv("data/Pedidos.csv")
df = pd.DataFrame(data)

# Função principal
def main():
    st.title("Dashboard de Vendas :shopping_trolley:")

    # Criação de abas
    aba1, aba2, aba3, aba4 = st.tabs(['Dataset', 'Receita', 'Vendedores', 'Métricas'])

    # Aba 1: Visualização do DataFrame
    with aba1:
        display_dataframe(df)

    # Aba 2: Visualização de Gráficos
    with aba2:
        display_charts(df)

    # Aba 3: Placeholder para aba de vendedores
    with aba3:
        st.header("Vendedores")
        st.write("Conteúdo para análise de vendedores.")

    # Aba 4: Exibir Métricas
    with aba4:
        display_metrics(df)

# Função para exibir o DataFrame
def display_dataframe(data):
    st.header("Visualização do DataFrame")
    
    # Filtros na barra lateral
    st.sidebar.header("Filtros")
    selected_region = st.sidebar.multiselect(
        "Selecione as regiões",
        data['Regiao'].unique(),
        data['Regiao'].unique()  # Todas as regiões selecionadas por padrão
    )
    
    # Filtrando os dados
    filtered_data = data[data['Regiao'].isin(selected_region)]
    
    # Exibindo os dados filtrados
    st.write(filtered_data)

# Função para exibir os gráficos
def display_charts(data):
    st.header("Visualização de Gráficos")
    
    # Gráfico 1: Desempenho por Região
    st.subheader("Desempenho por Região")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(x="Regiao", data=data, ax=ax)
    st.pyplot(fig)
    
    # Gráfico 2: Itens mais vendidos
    st.subheader("Itens mais Vendidos")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(x="Item", data=data, ax=ax)
    st.pyplot(fig)
    
    # Gráfico 3: Preço Médio por Item
    st.subheader("Preço Médio por Item")
    avg_price = data.groupby("Item")["PrecoUnidade"].mean().sort_values(ascending=False)
    st.bar_chart(avg_price)

# Função para exibir métricas
def display_metrics(data):
    st.subheader("Métricas")
    
    # Métricas simples
    total_sales = data["Unidades"].sum()
    average_price = data["PrecoUnidade"].mean()
    most_productive = data["Vendedor"].value_counts().idxmax()
    
    coluna1, coluna2, coluna3 = st.columns(3)
    with coluna1:
        st.metric("Vendedor mais produtivo", most_productive)
    with coluna2:
        st.metric("Vendas Totais", total_sales)
    with coluna3:
        st.metric("Preço Médio", round(average_price, 2))

# Garantindo que o script seja executado corretamente
if __name__ == "__main__":
    main()
