SELECT CdCli, NmCli, SUM(Qtd * VrUnt) AS Compras  FROM TbVendas
WHERE TbVendas.status NOT IN ('Em aberto','Cancelado') 
GROUP BY CdCli
HAVING SUM(Qtd * VrUnt) = (
SELECT MAX(soma)
FROM (
SELECT SUM(Qtd * VrUnt) soma FROM TbVendas
GROUP BY CdCli
)AS X)
;

