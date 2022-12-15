class Aviao:
    def __init__(self, modelo: str, velocidade_maxima: str, capacidade: str):
        self.__modelo = modelo
        self.__velocidade_maxima = velocidade_maxima
        self.__cor = 'Azul'
        self.__capacidade = capacidade
    
    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, valor:str):
        self.__modelo = valor

    @property
    def velocidade_maxima(self):
        return self.__velocidade_maxima

    @velocidade_maxima.setter
    def velocidade_maxima(self, valor:str):
        self.__velocidade_maxima = valor

    @property
    def capacidade(self):
        return self.__capacidade

    @capacidade.setter
    def capacidade(self, valor:str):
        self.__capacidade = valor
    @property
    def cor(self):
        return self.__cor

lista = []
for i in range(3):
    modelo = input('Qual modelo?: ')
    vel = input('Qual velocidade máxima: ')
    capacidade = input('Qual a capacidade: ')
    lista.append(Aviao(modelo,vel,capacidade))
for aviao in lista:
    print(f'O avião de modelo {aviao.modelo} possui uma velocidade máxima de {aviao.velocidade_maxima}, capacidade para {aviao.capacidade} passageiros e é da cor {aviao.cor}.')

