import csv
import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv

# 1. Caminhos dos arquivos locais
caminho_csv = r"C:\Users\CC\Desktop\SCTEC26\projeto_supermercado_set26\ETL\data\raw\supermarket_sales.csv.csv"
caminho_final_excel = r"C:\Users\CC\Desktop\SCTEC26\projeto_supermercado_set26\ETL\data\processed\vendas_tratadas.xlsx"

# 2. Leitura e tradução das colunas
df = pd.read_csv(caminho_csv, encoding="iso-8859-1")
traducao_colunas = {
    "Invoice ID": "id_venda", "Branch": "filial", "City": "cidade",
    "Customer type": "tipo_cliente", "Gender": "genero", "Product line": "linha_produto",
    "Unit price": "preco_unitario", "Quantity": "quantidade", "Tax 5%": "imposto",
    "Total": "valor_total", "Date": "data_venda", "Time": "hora_venda",
    "Payment": "forma_pagamento", "cogs": "custo_mercadoria", 
    "gross margin percentage": "margem_percentual", "gross income": "receita_bruta",
    "Rating": "avaliacao"
}
df = df.rename(columns=traducao_colunas)

# 3. Limpeza e correção das datas para o formato padrão do banco 
df = df.drop_duplicates()
df["data_venda"] = pd.to_datetime(df["data_venda"]).dt.strftime("%Y-%m-%d")

# 4. Salvando a tabela limpa em formato Excel na pasta processed
df.to_excel(caminho_final_excel, index=False)
print("Tabela de vendas limpa e salva com sucesso em formato Excel!")

# 5. Carga segura no banco lendo o arquivo .env da raiz do projeto
load_dotenv(os.path.join(os.path.dirname(__file__), "..", "..", ".env"))

try:
    print("Conectando ao banco de dados com credenciais protegidas...")
    conexao = psycopg2.connect(
        host=os.getenv("DB_HOST"), database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"), password=os.getenv("DB_PASS"),
        port=os.getenv("DB_PORT")
    )
    cursor = conexao.cursor()
    
    print("Limpando dados antigos da tabela vendas_tratada...")
    cursor.execute("TRUNCATE TABLE vendas_tratada;")
    
    print("Enviando novas linhas para o DBeaver...")
    
    for linha in df.astype(str).values.tolist():
        comando_dml = """
            INSERT INTO vendas_tratada (
                id_venda, filial, cidade, tipo_cliente, genero, linha_produto, 
                preco_unitario, quantidade, imposto, valor_total, data_venda, 
                hora_venda, forma_pagamento, custo_mercadoria, margem_percentual, 
                receita_bruta, avaliacao
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(comando_dml, linha)
        
    conexao.commit()
    print("Carga concluída com sucesso na tabela vendas_tratada!")
    
except Exception as erro:
    print(f"Erro na carga do banco: {erro}")
    if 'conexao' in locals(): conexao.rollback()
finally:
    if 'cursor' in locals(): cursor.close()
    if 'conexao' in locals(): conexao.close()
    print("Conexão encerrada com segurança.")