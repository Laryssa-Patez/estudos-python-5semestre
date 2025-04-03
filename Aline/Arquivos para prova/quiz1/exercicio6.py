# Função para verificar palíndromo
def eh_palindromo(texto):
    # Remove espaços e pontuações, converte para minúsculas
    import string
    texto = texto.lower()
    texto = texto.translate(str.maketrans('', '', string.punctuation + ' '))
    
    # Compara com sua versão invertida
    return texto == texto[::-1]

# Solicita entrada do usuário
texto = input("Digite uma string para verificar se é palíndromo: ")

# Verifica e exibe resultado
if eh_palindromo(texto):
    print(f"'{texto}' é um palíndromo!")
else:
    print(f"'{texto}' não é um palíndromo.")