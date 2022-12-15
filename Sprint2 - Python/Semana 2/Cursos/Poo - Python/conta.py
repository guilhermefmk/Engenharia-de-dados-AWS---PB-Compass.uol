from cliente import *
class Conta:

    def __init__(self, cod_conta: int,titular: Cliente, cpf: str, tipo_conta : int, saldo: float, limite : float):
        self.__cod_conta = cod_conta
        self.__titular = titular
        self.__cpf = cpf
        self.__tipo_conta = tipo_conta
        self.__saldo = saldo
        self.__limite = limite

    def deposita(self, quantia: float):
        if self.__saldo + quantia > self.__limite:
            print('Valor ultrapassa o limite')
        else: 
            self.__saldo += quantia
            print(f'Seu novo saldo é {self.__saldo}') 

    def saca(self,quantia:float):
        if self.__saldo - quantia < 0:
            print('Saldo insuficiente')
        else: 
            self.__saldo -= quantia
            print(f'Seu novo saldo é {self.__saldo}') 

    def transfere(self, conta, quantia: float):
        if self.__saldo - quantia < 0:
            print('Saldo insuficiente')
        else:
            if conta.__saldo + quantia > conta.__limite:
                print(f'Limite de {conta.__titular} insuficiente')
            else:
                conta.__saldo += quantia
                self.__saldo -= quantia
                print(f'saldo atual {conta.__saldo}')

    
    def get_tipo_conta(self):
        return self.__tipo_conta
    def get_saldo(self):
        return self.__saldo
    def get_limite(self):
        return self.__limite

    def set_tipo_conta(self, tipo_conta):
        self.__tipo_conta = tipo_conta
    def set_saldo(self, saldo):
        self.__saldo = saldo
    def set_limite(self, limite):
        self.__limite = limite
    



