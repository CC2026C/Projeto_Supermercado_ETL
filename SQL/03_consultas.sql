-- 1. CONSULTA BÁSICA: Selecionar colunas específicas 

SELECT 
    id_venda, 
    filial, 
    cidade, 
    tipo_cliente, 
    genero, 
    linha_produto, 
    preco_unitario, 
    quantidade
FROM vendas_tratada;

-- 2. FILTRAR DADOS - buscar compras com avaliações Nota >= 9.0
SELECT 
    id_venda, 
    cidade, 
    linha_produto, 
    avaliacao
FROM vendas_tratada
WHERE avaliacao >= 9.0;

-- 3. AGRUPAMENTO E SOMA: faturamento total por cidade
SELECT 
    cidade, 
    SUM(valor_total) AS faturamento_por_cidade,
    SUM(quantidade) AS total_produtos_vendidos
FROM vendas_tratada
GROUP BY cidade
ORDER BY faturamento_por_cidade DESC;


-- 4. MÉDIA ANALÍTICA (group by + AVG): avaliação média por linha de produto
SELECT 
    linha_produto,
    ROUND(AVG(preco_unitario), 2) AS preco_medio_produto,
    ROUND(AVG(avaliacao), 2) AS nota_media_consumidores
FROM vendas_tratada
GROUP BY linha_produto
ORDER BY nota_media_consumidores DESC;