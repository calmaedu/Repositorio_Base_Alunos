# Lendo um arquivo do tipo json
# Sempre iniciamos com a importanção do json ou da biblioteca que utilizarmos
import json
# Abriremos o arquivo e o modo "r" lê esse arquivo
with open("dados.json","r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo) # esse método json.load converte o
#conteúdo do arquivo json em um dicionaria
print(dados)
print(type(dados))

