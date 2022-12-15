SELECT NmPro PRODUTO, Estado ESTADO, AVG(Qtd) MEDIA
FROM TbVendas
WHERE status IN ('Concluído')
GROUP BY Estado, NmPro
ORDER BY Estado ASC;
