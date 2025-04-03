# Função para verificar se um número é perfeito
def numero_perfeito(num):
    # Verifica se o número é positivo
    if num <= 0:
        return False
    
    # Inicializa a soma dos divisores
    soma_divisores = 0
    
    # Itera de 1 até num-1 para encontrar divisores
    for i in range(1, num):
        # Se i é divisor de num, adiciona à soma
        if num % i == 0:
            soma_divisores += i
    
    # Retorna True se a soma dos divisores é igual ao número
    return soma_divisores == num

# Solicita entrada do usuário
num = int(input("Digite um número para verificar se é perfeito: "))

# Verifica e exibe o resultado
if numero_perfeito(num):
    print(f"{num} é um número perfeito!")
else:
    print(f"{num} não é um número perfeito.")