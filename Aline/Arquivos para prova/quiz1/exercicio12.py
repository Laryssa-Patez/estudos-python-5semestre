def maior_subsequencia_crescente(lista):
    if not lista:
        return 0
    
    max_tamanho = 1
    atual_tamanho = 1
    
    # Percorre a lista a partir do segundo elemento
    for i in range(1, len(lista)):
        # Se o elemento atual é maior que o anterior
        if lista[i] > lista[i-1]:
            atual_tamanho += 1
            max_tamanho = max(max_tamanho, atual_tamanho)
        else:
            atual_tamanho = 1
    
    return max_tamanho

# Solicita entrada do usuário
entrada = input("Digite os números separados por espaço: ")
numeros = list(map(int, entrada.split()))

# Calcula e exibe o resultado
tamanho = maior_subsequencia_crescente(numeros)
print(f"O tamanho da maior subsequência crescente contínua é {tamanho}")