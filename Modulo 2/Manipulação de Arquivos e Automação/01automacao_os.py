# Abrir e ler o arquivo 
Arquivo = open('hello.txt','r', encoding= 'utf-8') # abrindo o arquivo
conteudo = arquivo.read() # lendo o arquivo e armazenado na variavel

print(conteudo) # apresentando a leitura feita 
arquivo.closse() # fechando o arquivo

# retorna o tamanho do arquivo em bytes
import os
print(os.path.getsize('hello.txt'),"bytes")

#listar todos os arquivos e pastas de um diretoria
# não iremos importar a biblioteca os por que já fizemos isso neste script (arquivo)
print(os.listdir(".")) #lista todo o coteúdo da pasta atual

# separar diretórios e arquivos 
# não iremos diretórios e arquivos
caminho = "/home/user/documentos/arquivos.txt"
print(os.path.dirname(caminho)) # /home/user/documentos
print(os.path.basename(caminho)) # arquivo.txt

