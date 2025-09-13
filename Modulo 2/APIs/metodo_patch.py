# Método PATCH(atualização parcial)

import requests
url = "https://jsonplaceholder.typicode.com/posts/7"

atualizacao = {
    "title":"Título atualizado no exercício"
}

response = requests.patch(url, json=atualizacao)

print("status code:", response .status_code)
print("Respostas da API:",response.json())