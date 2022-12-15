
class Passaro:
    
    def voar(self):
        return 'Estou voando'

    def emitirSom(self):
        return 'Assoviando'


class Pardal(Passaro):
    
    def emitirSom(self):
        return 'Piu Piu Piu'


class Pato(Passaro):
    
    def emitirSom(self):
        return 'Quá Quá Quá'

pardal = Pardal()
pato = Pato()

print(pardal.emitirSom())
print(pato.emitirSom())