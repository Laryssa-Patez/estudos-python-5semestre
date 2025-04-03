# Função recursiva para calcular fatorial
def fatorial(n):
    # Caso base: fatorial de 0 ou 1 é 1
    if n == 0 or n == 1:
        return 1
    # Chamada recursiva: n! = n * (n-1)!
    else:
        return n * fatorial(n - 1)

# Solicita entrada do usuário
num = int(input("Digite um número para calcular seu fatorial: "))

# Verifica se o número é negativo
if num < 0:
    print("Fatorial não está definido para números negativos.")
else:
    resultado = fatorial(num)
    print(f"O fatorial de {num} é {resultado}")