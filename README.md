# Pipeline de ETL - Análise de Vendas de Supermercado

O projeto realiza a Extracao, Limpeza, Transformacao e Carga (ETL) dos dados de vendas de um supermercado, utilizando Python para o tratamento e PostgreSQL para o armazenamento seguro.

## Estrutura do Projeto

projeto_supermercado_set26/
│
├── .env                  # Credenciais ocultas do banco de dados
├── .gitignore            # Arquivo para ocultar senhas e dados locais
├── README.md             # Documentacao do projeto
├── requirements.txt      # Bibliotecas necessarias para o Python
│
├── sql/                  # Scripts de banco de dados do DBeaver
│   ├── 01_criar_banco.sql
│   ├── 02_criar_tabelas.sql
│   └── 03_consultas.sql
│
├── ETL/
│   ├── data/             # Pastas de armazenamento dos dados
│   │   ├── raw/          # CSV original com dados brutos
│   │   ├── processed/    # Tabela de vendas limpa em formato Excel (.xlsx)
│   │   └── gold_tratada/ # Indicadores calculados em formato Excel (.xlsx)
│   │
│   └── src/              # Scripts Python (.py) do processamento
│       ├── 01_leitura_dados.py
│       ├── 02_etl_vendas.py
│       ├── 03_estatistica.py
│       └── 04_visualizacao.py
│
└── resultados/           # Graficos analiticos salvos em formato .png

## Passo a Passo do Processo

1. **01_leitura_dados.py:** Faz a leitura inicial do arquivo bruto contido na pasta raw.
2. **02_etl_vendas.py:** Traduz as colunas, remove registros duplicados, padroniza as datas e exporta o resultado em formato Excel para a pasta processed. Também realiza a carga segura dos dados no PostgreSQL.
3. **03_estatistica.py:** Calcula o faturamento total e o ticket medio do supermercado, salvando o relatorio final em Excel na pasta gold_tratada.
4. **04_visualizacao.py:** Cria e salva de forma automatizada três graficos analiticos em portugues na pasta resultados.

## Seguranca de Credenciais

As informações de acesso ao banco de dados (host, usuario e senha) foram totalmente isoladas dentro do arquivo oculto `.env` na raiz do projeto. O script faz a leitura das credenciais direto na memoria e o arquivo `.gitignore` impede que a senha seja enviada para repositorios publicos.

## Resultados das Questoes de Negocio

- Filial com maior faturamento: Filial C
- Filial com maior quantidade de vendas: Filial A
- Linha de produto com maior faturamento: Alimentos e Bebidas
- Linha de produto com melhor avaliacao media: Alimentos e Bebidas
- Forma de pagamento mais utilizada: Carteira Digital (Ewallet)
- Valor medio das vendas (Ticket Medio): R\$ 322.97
- Maior venda registrada no supermercado: R\$ 1.042,65
- Dia da semana com maior quantidade de vendas: Sabado

## Como Executar o Projeto

1. Execute os scripts da pasta `sql/` no DBeaver para criar a estrutura do banco.
2. Crie o arquivo `.env` na raiz do projeto preenchido com a sua senha do PostgreSQL.
3. Instale as bibliotecas necessarias executando no terminal:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute individualmente os scripts da pasta `ETL/src/` na ordem numerica (do 01 ao 04).
