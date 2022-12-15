import datetime

x = datetime.datetime.now()

try:
    nome = input('Qual seu nome?\n')
    data = input('Qual sua data de nascimento(dd-mm-aaaa)?\n')
    dia = int(data[:2])
    mes = int(data[3:5])
    ano = int(data[6:10])
    idade = x.year - ano if x.month>mes else ((x.year - ano) -1 if x.month < mes else (x.year - ano if x.day >= dia else (x.year - ano) -1))
    print(f'Olá {nome}!\nVocê tem {idade} anos de idade e fará 100 anos em {dia}/{mes}/{ano+100}')
except:
    print("Ocorreu um erro")





