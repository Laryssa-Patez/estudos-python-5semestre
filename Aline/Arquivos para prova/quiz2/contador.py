def contador_palavras(texto):
    palavras = texto.split()  # O método split() sem argumentos divide por qualquer quantidade de espaços em branco
    return len(palavras)
    # Retorna o número de palavras encontradas
    # A função len() conta quantos elementos existem na lista 'palavras'
