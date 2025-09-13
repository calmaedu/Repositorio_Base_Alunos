# Api que apresenta imagens aleatórios de cachoros
import requests
url= 'https://dog.ceo/api/breeds/image/random'
 
response = requests.get(url)

print("Linke da imagem:", response.json()["message"])