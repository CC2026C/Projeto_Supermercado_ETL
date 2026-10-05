import csv
import os
import pandas as pd
import psycopg2


caminho_csv = r"C:\Users\CC\Desktop\SCTEC26\projeto_supermercado_set26\ETL\data\raw\supermarket_sales.csv.csv"

print("Caminho do arquivo configurado com sucesso.")

df_bruto = pd.read_csv(caminho_csv, encoding="iso-8859-1")

# Total de linhas e colunas detectadas
print(f"Total de linhas encontradas: {df_bruto.shape[0]}")
print(f"Total de colunas encontradas: {df_bruto.shape[1]}")

print("Amostra dos dados:")
print(df_bruto.head(3))




# Dados de conexão com  banco do DBeaver
DB_HOST = "localhost"
DB_NAME = "supermercado_db"
DB_USER = "postgres"        
DB_PASS = "postgres"
DB_PORT = "5432"

try:
    print("Conectando ao banco de dados...")
    conexao = psycopg2.connect(
        host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS, port=DB_PORT
    )
    cursor = conexao.cursor()
    
    print("Limpando dados antigos da tabela...")
    cursor.execute("TRUNCATE TABLE camada_raw;")
    
    print("Enviando linhas para o banco de dados...")
    contador = 0
    
    with open(caminho_csv, mode="r", encoding="iso-8859-1") as arquivo:
        leitor_fluxo = csv.reader(arquivo, delimiter=",")
        next(leitor_fluxo)  
        
        for linha in leitor_fluxo:
            comando_dml = """
                INSERT INTO camada_raw (
                    id_venda, filial, cidade, tipo_cliente, genero, linha_produto, 
                    preco_unitario, quantidade, imposto, valor_total, data_venda, 
                    hora_venda, forma_pagamento, custo_mercadoria, margem_percentual, 
                    receita_bruta, avaliacao
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """
            cursor.execute(comando_dml, linha)
            contador += 1
            
    conexao.commit()
    print(f"Carga concluída. Total de {contador} linhas salvas com sucesso.")

except Exception as erro:
    print(f"Erro ao conectar ou enviar dados: {erro}")
    if conexao:
        conexao.rollback()
        
finally:
    if 'cursor' in locals() and cursor: cursor.close()
    if 'conexao' in locals() and conexao: conexao.close()
    print("Conexão encerrada.")