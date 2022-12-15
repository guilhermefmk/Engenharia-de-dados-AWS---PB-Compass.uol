SELECT X.COD_VENDEDOR, X.VENDEDOR, X.CONTADOR FROM
(SELECT TbVendedor.CdVdd AS COD_VENDEDOR,TbVendedor.NmVdd AS VENDEDOR, COUNT(TbVendedor.CdVdd) CONTADOR FROM TbVendas
INNER JOIN
TbVendedor
ON TbVendedor.CdVdd = TbVendas.CdVdd AND TbVendas.status in ('Concluido')
group by TbVendedor.CdVdd
HAVING COUNT(TbVendedor.CdVdd)=(
SELECT MAX(Mycount)
FROM (
SELECT TbVendas.CdVdd, COUNT(TbVendas.CdVdd) Mycount
FROM TbVendas
WHERE TbVendas.status in ('Concluido')
GROUP BY TbVendas.CdVdd
) AS Y)) X;
