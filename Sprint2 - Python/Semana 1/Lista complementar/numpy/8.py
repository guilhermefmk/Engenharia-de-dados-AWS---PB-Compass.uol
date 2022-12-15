'''
Dado o array definido por np.arange(25).reshape(5, 5), realize as seguintes operações sem utilizar nenhum
tipo de loop (for / while):
• A média das linhas 0, 2 e 3.
• A média das colunas 0, 1 e 4.
• A soma dos elementos das duas diagonais.
'''

import numpy as np

array = np.arange(25).reshape(5, 5)

med_linha = np.mean(array, axis=1)
med_linha_zero = med_linha[0]
med_linha_dois = med_linha[2]
med_linha_tres = med_linha[3]

med_col = np.mean(array, axis=0)
med_col_zero = med_col[0]
med_col_um = med_col[1]
med_col_quatro = med_col[4]

print(med_linha_zero, med_linha_dois , med_linha_tres)

print(med_col_zero, med_col_um , med_col_quatro)