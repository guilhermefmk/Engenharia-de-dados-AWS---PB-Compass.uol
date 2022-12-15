SELECT Estado,(SUM(Qtd * VrUnt)/ COUNT(Estado)) `AVG` FROM TbVendas
WHERE status IN ('Concluído')
GROUP BY Estado;
