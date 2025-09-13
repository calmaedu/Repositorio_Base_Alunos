import json
# Convertendo um arquivo json em dicionário
# String no formato json, usar aspas duplas e os valores boolenos em minúsculo

json_python = '{"nome": "Ana","idade":30,"estudante":true}'

dados_python = json.loads(json_python) # lendo o arquivo

print(dados_python['nome']) # traz as informações armazenadas nas respectivas chaves
print(dados_python['idade'])
print(dados_python['estudante'])