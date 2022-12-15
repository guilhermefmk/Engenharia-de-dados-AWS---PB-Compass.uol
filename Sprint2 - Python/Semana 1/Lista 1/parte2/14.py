
import random

random_list = random.sample(range(500),50)
random_list.sort()

soma = 0

for x in random_list:
    soma += x

media = soma/len(random_list)


mediana = random_list[(len(random_list) // 2)] if len(random_list) % 2 != 0 else ((random_list[len(random_list) // 2]) + (random_list[len(random_list) // 2 - 1]))/2

print(f'{random_list}\nO valor minimo é {min(random_list)}\nO valor máximo é {max(random_list)}\nA média dos valores é {media:.2f}\nE sua mediana é {mediana}')

