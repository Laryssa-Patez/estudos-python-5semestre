import re # Importa o módulo de expressões regulares

def validar_telefone(telefone):
    padrao = r'^\(\d{2}\) \d{4,5}-\d{4}$'
    return re.match(padrao, telefone) is not None
    # re.match verifica se o telefone corresponde ao padrão
    # Retorna True se encontrar correspondência, False caso contrário




# Padrão regex para validar telefone:
    # ^         - Início da string
    # \(\d{2}\) - Código de área (DDD) entre parênteses, ex: (11)
    # \d{4,5}   - 4 ou 5 dígitos (para fixo ou celular)
    # -\d{4}    - Hífen seguido de 4 dígitos
    # $         - Fim da string