import datetime
dia = int(input('Dia?\n'))
mes = int(input('Mes?\n'))
ano = int(input('Ano?\n'))
x = datetime.datetime(ano, mes, dia)

print(x.strftime("%d/%m/%Y"))