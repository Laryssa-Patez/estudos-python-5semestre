import json
import os

# Nome do arquivo para armazenar os contatos
ARQUIVO_CONTATOS = 'contatos.json'

# Função para carregar contatos do arquivo
def carregar_contatos():
    # Verifica se o arquivo existe
    if os.path.exists(ARQUIVO_CONTATOS):
        # Abre o arquivo para leitura
        with open(ARQUIVO_CONTATOS, 'r', encoding='utf-8') as f:
            try:
                # Carrega os dados do arquivo JSON
                return json.load(f)
            except json.JSONDecodeError:
                # Se o arquivo estiver vazio ou corrompido, retorna um dicionário vazio
                return {}
    # Se o arquivo não existir, retorna um dicionário vazio
    return {}

# Função para salvar contatos no arquivo
def salvar_contatos(contatos):
    # Abre o arquivo para escrita
    with open(ARQUIVO_CONTATOS, 'w', encoding='utf-8') as f:
        # Salva os contatos no arquivo JSON
        json.dump(contatos, f, indent=4)

# Função para adicionar contato (agora usando arquivo)
def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    
    # Carrega os contatos existentes
    contatos = carregar_contatos()
    
    # Adiciona o novo contato
    contatos[nome] = telefone
    
    # Salva no arquivo
    salvar_contatos(contatos)
    print(f"Contato '{nome}' adicionado com sucesso!")

# Função para remover contato (agora usando arquivo)
def remover_contato():
    nome = input("Digite o nome do contato a ser removido: ")
    
    # Carrega os contatos existentes
    contatos = carregar_contatos()
    
    # Verifica se o contato existe
    if nome in contatos:
        # Remove o contato
        del contatos[nome]
        
        # Salva no arquivo
        salvar_contatos(contatos)
        print(f"Contato '{nome}' removido com sucesso!")
    else:
        print(f"Contato '{nome}' não encontrado.")

# Função para atualizar contato (agora usando arquivo)
def atualizar_contato():
    nome = input("Digite o nome do contato a ser atualizado: ")
    
    # Carrega os contatos existentes
    contatos = carregar_contatos()
    
    # Verifica se o contato existe
    if nome in contatos:
        novo_telefone = input("Digite o novo telefone: ")
        
        # Atualiza o telefone
        contatos[nome] = novo_telefone
        
        # Salva no arquivo
        salvar_contatos(contatos)
        print(f"Contato '{nome}' atualizado com sucesso!")
    else:
        print(f"Contato '{nome}' não encontrado.")

# Função para listar contatos (agora usando arquivo)
def listar_contatos():
    # Carrega os contatos existentes
    contatos = carregar_contatos()
    
    # Verifica se há contatos
    if not contatos:
        print("Nenhum contato cadastrado.")
    else:
        print("\nLista de contatos:")
        for nome, telefone in contatos.items():
            print(f"- {nome}: {telefone}")

# Menu principal
def main():
    while True:
        print("\n--- Sistema de Contatos (Arquivo) ---")
        print("1. Adicionar contato")
        print("2. Remover contato")
        print("3. Atualizar contato")
        print("4. Listar contatos")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_contato()
        elif opcao == '2':
            remover_contato()
        elif opcao == '3':
            atualizar_contato()
        elif opcao == '4':
            listar_contatos()
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    main()