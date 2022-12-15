class Pessoa:

    def __init__(self, nome: str, id: int):
        self.__nome = nome
        self.id = id
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

