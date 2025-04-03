import re #Permite fazer buscas, extrações e validações complexas em strings

def validar_email(email):
    """Valida emails incluindo addresses com + e bloqueando acentos"""
    
    # Primeiro verifica se o input NÃO é uma string
    # Isso protege contra erros se receber números, listas, None, etc.
    if not isinstance(email, str):
        return False # Retorna False imediatamente para não-strings
        
    # Define o padrão (regex) para validar o email:
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.fullmatch(padrao, email))
    # re.fullmatch() verifica se TODA a string corresponde ao padrão
    # bool() converte o resultado para True/False explícito