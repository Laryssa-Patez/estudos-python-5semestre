def encontrar_subconjuntos(numeros, alvo):
    from itertools import combinations
    
    resultados = []
    # Verifica todos os tamanhos possíveis de subconjuntos
    for r in range(1, len(numeros) + 1):
        # Gera todas as combinações de tamanho r
        for combo in combinations(numeros, r):
            # Se a soma da combinação é igual ao alvo
            if sum(combo) == alvo:
                resultados.append(list(combo))
    
    return resultados

# Solicita entrada do usuário
entrada = input("Digite os números separados por espaço: ")
numeros = list(map(int, entrada.split()))
alvo = int(input("Digite o valor alvo: "))

# Encontra e exibe os subconjuntos
subconjuntos = encontrar_subconjuntos(numeros, alvo)
print(f"Subconjuntos que somam {alvo}:")
for sub in subconjuntos:
    print(sub)