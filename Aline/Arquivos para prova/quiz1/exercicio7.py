# Função para gerar N termos da sequência de Fibonacci
def fibonacci(n):
    # Casos base
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    # Inicia a sequência
    sequencia = [0, 1]
    
    # Gera os próximos termos
    for i in range(2, n):
        proximo = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo)
    
    return sequencia

# Solicita entrada do usuário
n = int(input("Digite quantos termos da sequência de Fibonacci deseja: "))

# Obtém e exibe a sequência
seq = fibonacci(n)
print(f"Os {n} primeiros termos da sequência de Fibonacci são:")
print(seq)