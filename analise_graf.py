import os
import pandas as pd
import plotly.express as px

lista_arquivo = os.listdir(r"C:\Users\vanes\PycharmProjects\Curso_hashtag\Vendas")

#Importar as bases de dados de vendas
tabela_total = pd.DataFrame()

for arquivo in lista_arquivo:
 if "vendas" in arquivo.lower():
    tabela = pd.read_csv(fr"C:\Users\vanes\PycharmProjects\Curso_hashtag\Vendas{arquivo}")
    tabela_total = tabela_total._append(tabela)

#Tratar/Compilar as bases de dados

print(tabela_total)

#Calcular o produto mais vendido (em quantidade)

tabela_produtos = tabela_total.groupby("Produto").sum()
tabela_produtos = tabela_produtos[["Quantidade Vendida"]].sort_values(by="Quantidade Vendida", ascending=False)
print(tabela_produtos)

#Calcular o produto que mais faturou (em faturamento)

tabela_total["Faturamento"] = tabela_total["Quantidade Vendida"] * tabela_total["Preco Unitario"]
tabela_faturamento = tabela_total.groupby("Produto").sum()
tabela_faturamento = tabela_faturamento[["Faturamento"]].sort_values(by="Faturamento", ascending=False)
print(tabela_faturamento)

#Calcular a loja/cidade que mais vendeu (em faturamento) - criar um grafico/dashboard

tabela_lojas = tabela_total.groupby("Loja").sum()
tabela_lojas = tabela_lojas[["Faturamento"]].sort_values(by="Faturamento", ascending=False)
print(tabela_lojas)

grafico = px.bar(tabela_lojas, x=tabela_lojas.index , y="Faturamento")
grafico.show()