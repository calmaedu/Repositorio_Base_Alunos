# Criar um código que consuma uma api de clima e informe
# A temperatura e a descrição do clime em um lugar especifíco

import requests

cidade = input("Digite o nome da cidade: ").strip()
api_Key = '2a1ac38a32354cb7b19133643251408'
url = f'https://api.weatherapi.com/v1/current.json'


#2. parametros da requisição 
parametros = {
    'Key':api_Key,
    'q':cidade,
    'lang':'pt' # define a lígua da resposta como portugues do Brasil
}

#3. Fazer a requisição
resposta = requests.get(url, params=parametros)

#4. Verificar se a requisição foi bem sucedida
if resposta.status_code == 200:
    dados = resposta.json()
    temperatura = dados['current']['temp_c']
    descricao =dados['current']['condition']['text']
    print(f' temperatura na cidade {cidade} é {temperatura}°c.')
    print(f'Descrição: {descricao}')
else:
    print(f'Erro na requisição: {resposta.status_code}')
    print(resposta.content)
