import os
import pandas as pd
import matplotlib.pyplot as plt

# 1. Caminhos para ler do Excel
caminho_dados = r"C:\Users\CC\Desktop\SCTEC26\projeto_supermercado_set26\ETL\data\processed\vendas_tratadas.xlsx"
pasta_resultados = r"C:\Users\CC\Desktop\SCTEC26\projeto_supermercado_set26\resultados"

# 2. Ler arquivo 
df_vendas = pd.read_excel(caminho_dados)

# Garante o nome correto em portugues da coluna de valores caso venha em ingles
if "Sales" in df_vendas.columns:
    df_vendas = df_vendas.rename(columns={"Sales": "valor_total"})

print("Dados carregados com sucesso do Excel para a geracao dos graficos.")


# GRAFICO 1: Faturamento por Filial 

faturamento_filial = df_vendas.groupby("filial")["valor_total"].sum()
faturamento_filial.plot(kind="bar", color="blue")

plt.title("Faturamento Total por Filial")
plt.xlabel("Filiais")
plt.ylabel("Faturamento em R$")
plt.tight_layout()
plt.savefig(os.path.join(pasta_resultados, "faturamento_filial.png"))
plt.close()
print("Grafico 1 (Filiais) gerado com sucesso!")


# GRAFICO 2: Faturamento por Linha de Produto 

traducao_produtos = {
    "Health and beauty": "Saude e Beleza",
    "Electronic accessories": "Acessorios Eletronicos",
    "Home and lifestyle": "Casa e Estilo de Vida",
    "Sports and travel": "Esportes e Viagens",
    "Food and beverages": "Alimentos e Bebidas",
    "Fashion accessories": "Acessorios de Moda"
}
df_vendas["linha_produto"] = df_vendas["linha_produto"].replace(traducao_produtos)

faturamento_produto = df_vendas.groupby("linha_produto")["valor_total"].sum()
faturamento_produto.plot(kind="bar", color="green")

plt.title("Faturamento Total por Linha de Produto")
plt.xlabel("Linhas de Produtos")
plt.ylabel("Faturamento em R$")
plt.tight_layout()

plt.savefig(os.path.join(pasta_resultados, "faturamento_produto.png"))
plt.close()
print("Grafico 2 (Produtos) gerado com sucesso!")

# GRAFICO 3: Formas de Pagamento Mais Utilizadas 

traducao_pagamentos = {
    "Ewallet": "Carteira Digital",
    "Cash": "Dinheiro",
    "Credit card": "Cartao de Credito"
}
df_vendas["forma_pagamento"] = df_vendas["forma_pagamento"].replace(traducao_pagamentos)

uso_pagamento = df_vendas["forma_pagamento"].value_counts()
uso_pagamento.plot(kind="pie", autopct="%1.1f%%")

plt.title("Divisao das Formas de Pagamento Utilizadas")
plt.ylabel("")
plt.tight_layout()

plt.savefig(os.path.join(pasta_resultados, "formas_pagamento.png"))
plt.close()
print("Grafico 3 (Pizza de Pagamentos) gerado com sucesso!")

print("Todos os graficos atualizados.")