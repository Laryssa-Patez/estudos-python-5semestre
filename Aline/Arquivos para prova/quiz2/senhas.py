import re #Permite fazer buscas, extrações e validações complexas em strings

def senha_segura(senha):
    if len(senha)<8: #Retorna o número de itens em um objeto (para strings, conta os caracteres)
        return False #senha muito curta
    
    if not re.search(r"[A-Z]", senha):
        return False
    
    if not re.search(r"[a-z]", senha):
        return False
    
    if not re.search(r"[0-9]", senha):
        return False
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        return False
    
    return True