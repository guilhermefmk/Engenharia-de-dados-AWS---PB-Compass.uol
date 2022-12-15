import json

file = open("/home/guilherme.cunha/Área de Trabalho/WORKSPACE/Compass/Sprint2/archives/person.json",'r')
conteudo = file.read()
dados= json.loads(conteudo)

print(dados['path'])

