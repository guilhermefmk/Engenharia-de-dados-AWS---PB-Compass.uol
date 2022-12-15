'''
    O código irá realizar as análises acima baseado no arquivo 'actors.csv', o caminho para a pasta em que o arquivo se encontra
    deve ser inserido na váriavel 'path_actors', logo abaixo.
'''
path_dir = 'Desafio/'
<<<<<<< HEAD:Sprint2/Semana 2/Desafio/desafio_procedural.py
# Criando matriz de dados
=======

>>>>>>> refs/remotes/origin/main:Sprint2/Semana 2/Desafio/desafio.py
with open(f'{path_dir}actors.csv', 'r') as f:
    dados = []
    dados_series = []
    for indice, line in enumerate(f):  
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

    # Ajustando valor de "Robert Downey, Jr"
    dados[4][0] += dados[4][1]
    del dados[4][1]
    dados[4][0] = dados[4][0].replace('"','')
    
    # Criando Series
    for i in range(len(colunas)):
        dados_series.append([])
    for linha in dados:
        for indice, item in enumerate(linha):
            dados_series[indice].append(item)

    # Convertendo tipos de dados
    dados_series[1] = [float(x) for x in dados_series[1]]
    dados_series[2] = [int(x) for x in dados_series[2]]
    dados_series[3] = [float(x) for x in dados_series[3]]
    dados_series[5] = [float(x) for x in dados_series[5]]
    
  
    # Ator ou atriz com maior núemro de filmes
    mais_filmes = max(dados_series[2])
    index = dados_series[2].index(mais_filmes)
    
    with open(f'{path_dir}1.txt','w') as g:
        for indice, series in enumerate(dados_series):
            g.write(colunas[indice] + ' ' + str(series[index]) + ' \n')
        g.close()
        
    
    # A média do número de filmes por autor.
<<<<<<< HEAD:Sprint2/Semana 2/Desafio/desafio_procedural.py
=======

>>>>>>> refs/remotes/origin/main:Sprint2/Semana 2/Desafio/desafio.py
    with open(f'{path_dir}2.txt','w') as g:
        for ator in set(dados_series[0]):
            indices = [ x for x in range(len(dados_series[0])) if dados_series[0][x] == ator ]
            soma = 0
            for index in indices:
                soma += dados_series[2][index]
            g.write(ator + ' ' + str(soma/len(indices)) + '\n')
        g.close()


    

    # O ator/atriz com a maior média por filme.
    maior_avg = max(dados_series[3])
    index1 = dados_series[3].index(maior_avg)

    with open(f'{path_dir}3.txt','w') as g:
        for indice, series in enumerate(dados_series):
            g.write(colunas[indice] + ' ' + str(series[index1]) + ' \n')
        g.close()
    
    contador_mais_vezes = 0
    for x in set(dados_series[4]):
        if (dados_series[4].count(x)) > contador_mais_vezes:
            contador_mais_vezes = dados_series[4].count(x)
            filme_mais_vezes = x

    with open(f'{path_dir}4.txt','w') as g:
            g.write('Movie ' + filme_mais_vezes + '\nCount ' + str(contador_mais_vezes))
            g.close()
   
    # Ator ou atriz mais bem pago
    mais_bem_pago = max(dados_series[1])
    index3 = dados_series[1].index(mais_bem_pago)

    with open(f'{path_dir}5.txt','w') as g:
        for indice, series in enumerate(dados_series):
            g.write(colunas[indice] + ' ' + str(series[index3]) + ' \n')
        g.close()
    
    f.close()

