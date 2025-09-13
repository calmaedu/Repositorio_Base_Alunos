# Método POST (adicionar/criar)

import requests
url ="https://jsonplaceholder.typicode.com/posts"

novo_post={
    "Títle":"Meu primeiro POST",
    "Body":"Estou aprendendo a enviar dados com python",
    "userId":10
}
# Criando a requisição
response = requests.post(url, json=novo_post)

print("Status code: ",response.status_code)
print("Resosta da API; ",response.json())
