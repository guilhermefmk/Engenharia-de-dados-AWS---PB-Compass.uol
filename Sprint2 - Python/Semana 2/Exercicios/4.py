from ast import Or


class Ordenadora:

    def __init__(self, lista_baguncada):
        self.__lista_baguncada = lista_baguncada

    @property
    def lista_baguncada(self):
        return self.__lista_baguncada

    @lista_baguncada.setter
    def lista_baguncada(self, valor):
        self.__lista_baguncada - valor

    
    def ordenacaoCrescente(self):
        return sorted(self.lista_baguncada)

    def ordenacaoDecrescente(self):
        return sorted(self.lista_baguncada,reverse=True)



crescente = Ordenadora([3,4,2,1,5])
decrescente = Ordenadora([9,7,6,8])

print(crescente.ordenacaoCrescente())
print(decrescente.ordenacaoDecrescente())
