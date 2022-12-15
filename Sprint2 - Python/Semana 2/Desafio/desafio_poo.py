'''
    Essa classe visa trabalhar como a lib Pandas
    porém com listas, onde:
        * dados = uma matriz onde cada indice é uma lista com os valores de cada linha do csv importado
        * colunas = é uma lista que contém a primeira linha do csv importado
        * dados_series = uma matriz onde cada linha é uma lista com os valores de cada coluna agrupados

    Aqui busco trabalhar da melhor forma com as series, onde tenho por verdade que cada indice y em dados_series[0], por exemplo, corresponde ao dados
    no indice y em dados_series[1].   
'''
class DataFrame():

    def __init__(self, path_csv:str):
        self.__path_csv = path_csv
        self.dados = []
        self.colunas = []
        self.dados_series = []
        self.__csv_to_list_col_dados(self.path_csv)
        self.__dados_to_series()
    
    @property    
    def path_csv(self):
        return self.__path_csv 

    @path_csv.setter    
    def path_csv(self, value):
        self.__path_csv = value   
    
    def __csv_to_list_col_dados(self,path):
            with open(f'{path}', 'r') as csv:
                dados = []
                for indice, line in enumerate(csv):  
                    if indice > 0:
                        itens = line.split(',')
                        itens[-1] = itens[-1].replace("\n","")
                        itens[-1] = itens[-1].replace(" ","")
                        dados.append(itens[:])
                    else:
                        itens = line.split(',')
                        itens[-1] = itens[-1].replace("\n","")
                        itens[-1] = itens[-1].replace(" ","")
                        colunas = itens[:]
            for linha in dados:
                if len(linha) > len(dados[0]):
                    dados.pop(dados.index(linha))
            self.dados = dados
            self.colunas = colunas
    
    def __dados_to_series(self):
        for i in range(len(self.colunas)):
            self.dados_series.append([])       
        for linha in self.dados:
            for indice, item in enumerate(linha):
                self.dados_series[indice].append(item)

    # printa o calor de N colunas passadas no parametro COLUNAS separadas pelo valor passado no parametro SEP
    def print_column_items(self, colunas: list, sep: str):
        indices = self.list_of_index(colunas)
        saida = ''
        for line in self.dados:
            for pos, index in enumerate(indices):
                if pos >= len(indices)-1:
                    saida += f"{line[index]}"
                else:
                    saida += f"{line[index]}{sep}"
            saida += f"\n"
        return saida

    # retorna uma lista de valores da coluna passada no parametro COLUNA
    def get_column_items(self, coluna: str):
        index = self.list_of_index([coluna])
        return actors.dados_series[index[0]]

    # Converte o tipo de dados presente em N listas para int, float ou str, essa coluna neste objeto é caracterizada por um lista da
    # matriz dados_series
    def convert_type(self, colunas: list, type:str):
        indices = self.list_of_index(colunas)

        for index in indices:
            lista = []
            for item in self.dados_series[index]:
                try:
                    if type == 'float':
                        lista.append(float(item))
                    elif type == 'int':
                        lista.append(int(item))
                    elif type == 'str':
                         lista.append(str(item))
                    else:
                        return print('Conversões apenas para (str),(float) ou (int)')
                except:
                    return print('Erro de conversão para float, verifique os dados')
            self.dados_series[index] = lista
        return(print(f'Dados convertidos para {type}'))

    # Retorna uma lista dos indices das colunas passadas dentro do parametro COLUNAS
    def list_of_index(self, colunas:list):
        indices = []
        for col in colunas:
            indices.append(self.colunas.index(col))
        return indices

actors = DataFrame('Desafio/actors.csv')

# Convertendo dados
actors.convert_type(['Gross','Total Gross','Average per Movie'], 'float')
actors.convert_type(['Number of Movies'], 'int')

## O ator/atriz com maior número de filmes e o respectivo número de filmes.
mais_filmes = int(max(actors.get_column_items('Number of Movies')))
index = actors.dados_series[actors.list_of_index(['Number of Movies'])[0]].index(mais_filmes)
with open(f'Desafio/Exercicio1.txt','w') as g:
    for indice, series in enumerate(actors.dados_series):
        g.write(actors.colunas[indice] + ' ' + str(series[index]) + ' \n')

## A média do número de filmes por ator.
with open(f'Desafio/Exercicio2.txt','w') as g:
    coluna_ator = actors.dados_series[actors.list_of_index(['Actor'])[0]]
    coluna_nfilmes = actors.dados_series[actors.list_of_index(['Number of Movies'])[0]]
    for ator in set(coluna_ator):
        indices = [ x for x in range(len(coluna_ator)) if coluna_ator[x] == ator ]
        soma = 0
        for index in indices:
            soma += coluna_nfilmes[index]
        g.write(ator + ' ' + str(soma/len(indices)) + '\n')
    g.close()

## O ator/atriz com a maior média por filme.
maior_avg = float(max(actors.get_column_items('Average per Movie')))
index1 = actors.dados_series[actors.list_of_index(['Average per Movie'])[0]].index(maior_avg)
with open(f'Desafio/Exercicio3.txt','w') as g:
    for indice, series in enumerate(actors.dados_series):
        g.write(actors.colunas[indice] + ' ' + str(series[index1]) + ' \n')
    g.close()

## O nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.
contador_mais_vezes = 0
lista_filmes = actors.get_column_items('#1 Movie')
for filme in set(lista_filmes):
    if (lista_filmes.count(filme)) > contador_mais_vezes:
        contador_mais_vezes = lista_filmes.count(filme)
        filme_mais_vezes = filme
with open(f'Desafio/Exercicio4.txt','w') as g:
        g.write('Movie ' + filme_mais_vezes + '\nCount ' + str(contador_mais_vezes))
        g.close()

## O ator mais bem pago
mais_bem_pago = float(max(actors.get_column_items('Total Gross')))
index3 = actors.dados_series[actors.list_of_index(['Total Gross'])[0]].index(mais_bem_pago)
with open(f'Desafio/Exercicio5.txt','w') as g:
    for indice, series in enumerate(actors.dados_series):
        g.write(actors.colunas[indice] + ' ' + str(series[index3]) + ' \n')
    g.close()
