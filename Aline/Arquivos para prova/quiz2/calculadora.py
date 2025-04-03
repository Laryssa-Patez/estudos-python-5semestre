def somar(a,b): #def -> define a função
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero.") #lança um erro se tentar dividir por 0
    return a / b