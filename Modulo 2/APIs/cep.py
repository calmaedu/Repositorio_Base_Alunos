# instalar a bibliotaca requests através do comando: pip install requests (no terminal)
# importar a biblioteca para o arquivo de trabalho

import requests

# Solicitar os dados de entrada
cep = input('Digite o cep(somente némeros):')

url = f'https://viacep.com.br/ws/{cep}/json'

resposta = requests.get(url) # aqui estamos fazendo a requisição

if resposta.status_code == 200:
    dados = resposta.json()
    if 'erro' not in dados:
        print(f'CEP:{dados['cep']}')
        print(f'Logradourou:{dados['logradouro']}')
        print(f'Cidade:{dados['localidade']}')
        print(f'Estado:{dados['uf']}')
    else:
        print('CEP não foi encontrado')
else:
    print(f'Erro na requisição: {resposta.status_code}.')
    print(resposta.content)