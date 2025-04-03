# Dicionário para armazenar contatos
contatos = {}

# Função para adicionar contato
def adicionar_contato(nome, telefone):
    contatos[nome] = telefone
    print(f"Contato {nome} adicionado com sucesso!")

# Função para remover contato
def remover_contato(nome):
    if nome in contatos:
        del contatos[nome]
        print(f"Contato {nome} removido com sucesso!")
    else:
        print(f"Contato {nome} não encontrado.")

# Função para atualizar contato
def atualizar_contato(nome, novo_telefone):
    if nome in contatos:
        contatos[nome] = novo_telefone
        print(f"Contato {nome} atualizado com sucesso!")
    else:
        print(f"Contato {nome} não encontrado.")

# Função para listar contatos
def listar_contatos():
    if not contatos:
        print("Nenhum contato cadastrado.")
    else:
        print("Lista de contatos:")
        for nome, telefone in contatos.items():
            print(f"- {nome}: {telefone}")

# Menu interativo
while True:
    print("\nMenu:")
    print("1. Adicionar contato")
    print("2. Remover contato")
    print("3. Atualizar contato")
    print("4. Listar contatos")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        nome = input("Nome do contato: ")
        telefone = input("Telefone do contato: ")
        adicionar_contato(nome, telefone)
    elif opcao == '2':
        nome = input("Nome do contato a remover: ")
        remover_contato(nome)
    elif opcao == '3':
        nome = input("Nome do contato a atualizar: ")
        novo_telefone = input("Novo telefone: ")
        atualizar_contato(nome, novo_telefone)
    elif opcao == '4':
        listar_contatos()
    elif opcao == '5':
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")