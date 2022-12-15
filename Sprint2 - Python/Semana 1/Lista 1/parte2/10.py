





class Lampada(object):


    def __init__(self, ligada: bool):
        self.ligada = ligada


    def liga(self):
        if not self.ligada:
            self.set_ligada(True)
            print('Foi ligada')
        else:
            print('Já está ligada')


    def desliga(self):
        if not (self.ligada):
            print('Já está desligada')
        else:
            self.set_ligada(False)
            print('Foi desligada')

    def esta_ligada(self):
        return 'Está ligada' if self.ligada == True else 'Está desligada'

    def set_ligada(self, status):
        self.ligada = status



instance = Lampada(False)

print(instance.esta_ligada())