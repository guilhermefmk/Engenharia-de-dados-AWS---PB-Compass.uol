'''
Crie um array 5x5 com a sequência de números pares entre 0...50 (incluso) e faça as seguintes operações:
• Soma das linhas
• Soma das Colunas
• Média dos elementos da última linha
• Média dos elementos da última coluna
'''


import numpy as np


array = np.arange(2,51,2).reshape(5,5)
sum_column = np.sum(array, axis=0)
sum_line = np.sum(array, axis=1)

med_linha = np.mean(array, axis=1)
med_ultima_linha = med_linha[-1]
med_coluna = np.mean(array, axis=0)
med_ultima_coluna = med_coluna[-1]
# Array
print(array)
# Soma das linhas
print(sum_line)
# Soma das colunas
print(sum_column)
# Média da última linha
print(med_ultima_linha)
#Média da última coluna
print(med_ultima_coluna)
