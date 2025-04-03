# Função para verificar se um número é primo
def eh_primo(n):
    if n <= 1:
        return False
    # Verifica divisores de 2 até a raiz quadrada de n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Função principal que retorna primos entre dois números
def primos_entre(a, b):
    # Garante que a é o menor número
    if a > b:
        a, b = b, a
    
    # Lista para armazenar primos
    lista_primos = []
    
    # Verifica cada número no intervalo
    for num in range(a, b + 1):
        if eh_primo(num):
            lista_primos.append(num)
    
    return lista_primos

# Solicita entrada do usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Obtém e exibe os primos
primos = primos_entre(num1, num2)
print(f"Números primos entre {num1} e {num2}:")
print(primos)