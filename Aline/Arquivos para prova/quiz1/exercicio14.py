def elemento_majoritario(lista):
    if not lista:
        return None
    
    contagem = {}
    # Conta a ocorrência de cada elemento
    for num in lista:
        if num in contagem:
            contagem[num] += 1
        else:
            contagem[num] = 1
    
    # Verifica qual elemento aparece mais da metade das vezes
    metade = len(lista) // 2
    for num, count in contagem.items():
        if count > metade:
            return num
    
    return None

# Solicita entrada do usuário
entrada = input("Digite os números separados por espaço: ")
numeros = list(map(int, entrada.split()))

# Encontra e exibe o elemento majoritário
majoritario = elemento_majoritario(numeros)
if majoritario is not None:
    print(f"O elemento majoritário é {majoritario}")
else:
    print("Não há elemento majoritário na lista.")