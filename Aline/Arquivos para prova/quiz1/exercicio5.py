# Solicita o nome do arquivo
nome_arquivo = input("Digite o nome do arquivo .txt: ")

try:
    # Abre o arquivo em modo leitura
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        # Lê todas as linhas
        linhas = arquivo.readlines()
        
        # Conta linhas
        num_linhas = len(linhas)
        
        # Conta palavras e caracteres
        num_palavras = 0
        num_caracteres = 0
        
        for linha in linhas:
            palavras = linha.split()
            num_palavras += len(palavras)
            num_caracteres += len(linha)
        
        # Exibe resultados
        print(f"O arquivo contém:")
        print(f"- {num_linhas} linhas")
        print(f"- {num_palavras} palavras")
        print(f"- {num_caracteres} caracteres")

except FileNotFoundError:
    print("Arquivo não encontrado!")