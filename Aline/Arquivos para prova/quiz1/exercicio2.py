# Solicita texto do usuário
texto = input("Digite um texto: ")

# Remove pontuações e converte para minúsculas para padronização
import string
texto = texto.lower()
texto = texto.translate(str.maketrans('', '', string.punctuation))

# Divide o texto em palavras
palavras = texto.split()

# Dicionário para armazenar contagem
contagem_palavras = {}

# Conta cada palavra
for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

# Exibe o resultado
print("Contagem de palavras:")
print(contagem_palavras)