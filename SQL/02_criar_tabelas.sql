-- 1. TABELA RAW (Cópia fiel do seu CSV em português)
CREATE TABLE camada_raw (
    id_venda VARCHAR(100),
    filial VARCHAR(100),
    cidade VARCHAR(200),
    tipo_cliente VARCHAR(100),
    genero VARCHAR(50),
    linha_produto VARCHAR(250),
    preco_unitario VARCHAR(100),
    quantidade VARCHAR(100),
    imposto VARCHAR(100),
    valor_total VARCHAR(100),
    data_venda VARCHAR(100),
    hora_venda VARCHAR(100),
    forma_pagamento VARCHAR(100),
    custo_mercadoria VARCHAR(100),
    margem_percentual VARCHAR(100),
    receita_bruta VARCHAR(100),
    avaliacao VARCHAR(100)
);

-- 2. TABELA TRATADA (Estrutura final com as restrições do seu dicionário)
CREATE TABLE vendas_tratada (
    id_venda VARCHAR(50) NOT NULL PRIMARY KEY,
    filial VARCHAR(10) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    tipo_cliente VARCHAR(50),
    genero VARCHAR(20), 
    linha_produto VARCHAR(150) NOT NULL,
    preco_unitario NUMERIC(10,2) NOT NULL CHECK (preco_unitario >= 0),
    quantidade INTEGER NOT NULL CHECK (quantidade > 0),
    imposto NUMERIC(10,2) NOT NULL CHECK (imposto >= 0),
    valor_total NUMERIC(12,2) NOT NULL CHECK (valor_total >= 0),
    data_venda DATE NOT NULL,
    hora_venda TIME NOT NULL,
    forma_pagamento VARCHAR(50) NOT NULL,
    custo_mercadoria NUMERIC(12,2) NOT NULL CHECK (custo_mercadoria >= 0),
    margem_percentual NUMERIC(10,2),
    receita_bruta NUMERIC(12,2) NOT NULL CHECK (receita_bruta >= 0),
    avaliacao NUMERIC(4,2) CHECK (avaliacao >= 0 AND avaliacao <= 10)
);
