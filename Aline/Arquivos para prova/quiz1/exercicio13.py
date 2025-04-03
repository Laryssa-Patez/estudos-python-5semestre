def rotacionar_matriz(matriz):
    # Verifica se é matriz quadrada
    n = len(matriz)
    for linha in matriz:
        if len(linha) != n:
            raise ValueError("A matriz deve ser quadrada (NxN)")
    
    # Cria matriz vazia para o resultado
    rotacionada = [[0 for _ in range(n)] for _ in range(n)]
    
    # Preenche a matriz rotacionada
    for i in range(n):
        for j in range(n):
            rotacionada[j][n-1-i] = matriz[i][j]
    
    return rotacionada

# Exemplo de uso
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz original:")
for linha in matriz:
    print(linha)

rotacionada = rotacionar_matriz(matriz)
print("\nMatriz rotacionada 90 graus:")
for linha in rotacionada:
    print(linha)