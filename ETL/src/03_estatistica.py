import os
import pandas as pd

# Caminhos configurados para ler do processed e salvar em Excel na pasta gold_tratada
caminho_processed = r"C:\Users\CC\Desktop\SCTEC26\projeto_supermercado_set26\ETL\data\processed\vendas_tratadas.xlsx"
caminho_final_gold = r"C:\Users\CC\Desktop\SCTEC26\projeto_supermercado_set26\ETL\data\gold_tratada\indicadores_faturamento.xlsx"

df_limpo = pd.read_excel(caminho_processed)

print("Dados limpos carregados na memória para a análise estatística.")
print(f"Total de linhas prontas para cálculo: {len(df_limpo)}")

# Traduzir a coluna 'Sales' para 'valor_total' 
if "Sales" in df_limpo.columns:
    df_limpo = df_limpo.rename(columns={"Sales": "valor_total"})

# Cálculos do faturamento e ticket médio
faturamento_total = df_limpo["valor_total"].sum()
ticket_medio = df_limpo["valor_total"].mean()

# Estrutura a tabela de indicadores finais
df_gold = pd.DataFrame({
    "indicador": ["faturamento_total", "ticket_medio"],
    "valor_reais": [faturamento_total, ticket_medio]
})

# Exportar o relatório final da Camada Gold em formato Excel 
df_gold.to_excel(caminho_final_gold, index=False)
print("Sucesso! Indicadores estatísticos salvos em Excel na pasta gold_tratada.")