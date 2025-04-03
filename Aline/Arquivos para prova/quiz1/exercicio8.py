import random

# Solicita lista de nomes
entrada = input("Digite os nomes separados por vírgula: ")
nomes = [nome.strip() for nome in entrada.split(',')]

# Verifica se há nomes
if not nomes:
    print("Nenhum nome foi fornecido.")
else:
    # Sorteia um nome aleatoriamente
    sorteado = random.choice(nomes)
    print(f"O nome sorteado foi: {sorteado}")