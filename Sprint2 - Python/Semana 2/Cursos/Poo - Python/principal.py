from cliente import *
from conta import *

guilherme = Cliente('Guilherme')
conta1 = Conta(123,guilherme,'03774993076',1,1000,1000)
conta2 = Conta(323,'Alencar','03774993476',1,500,1000)

conta1.transfere(conta2, 1000)

print(guilherme.nome)