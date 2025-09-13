# metodo GET utilizando um api de teste
# esse método busca(get) alguma informação
import requests 
url = 'https://jsonplaceholder.typicode.com/posts/5'
response = requests.get(url)

print("Status:",response.status_code)
print("Título do post:",response.json()['title'])
