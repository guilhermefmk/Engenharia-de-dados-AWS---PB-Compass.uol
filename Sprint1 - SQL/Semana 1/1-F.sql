SELECT TbVendas.CdPro AS COD_PRODUTO,TbVendas.NmPro AS PRODUTO, COUNT(CASE WHEN TbVendas.NmCanalVendas = 'Matriz' THEN TbVendas.CdCanalVendas END) AS MATRIZ, COUNT(CASE WHEN TbVendas.NmCanalVendas = 'Ecommerce' THEN TbVendas.CdCanalVendas END) AS ECOMERCE 
FROM TbVendas
INNER JOIN TbEstoqueProduto
ON TbEstoqueProduto.CdPro = TbVendas.CdPro AND TbVendas.status IN ('Concluído')
GROUP BY PRODUTO
ORDER BY MATRIZ, ECOMERCE ASC
LIMIT 10;
