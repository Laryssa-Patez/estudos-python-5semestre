# Importa o módulo pytest - framework de testes
import pytest

# Importa o módulo os - fornece funções para interagir com o sistema operacional
import os

# Importa o módulo sys - fornece acesso a variáveis e funções relacionadas ao interpretador Python
import sys

# Adiciona o diretório atual ao Python Path (sys.path)
# Isso é necessário para que o Python encontre seus módulos locais durante a importação

# os.path.dirname(__file__) - pega o diretório do arquivo atual
# os.path.abspath() - converte para o caminho absoluto
# sys.path.insert(0, ...) - adiciona no início da lista de paths do Python
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Agora podemos importar as funções do módulo calculadora
# Isso só funciona porque adicionamos o diretório ao sys.path acima
from calculadora import somar, subtrair, multiplicar, dividir

#calculadora: Refere-se ao arquivo calculadora.py que você criou
#O Python automaticamente associa o nome calculadora ao arquivo calculadora.py

#somar, subtrair, multiplicar, dividir: São exatamente os nomes das funçõe
#que você definiu dentro do arquivo calculadora.py
#O Python vai procurar essas funções dentro do arquivo

def test_somar():
    assert somar(2, 3) == 5 #assert verifica se a condicao é verdadeira

    assert somar(-1, 1) == 0

    assert somar(-1, -1) == -2

def test_subtrair():
    assert subtrair(5, 3) == 2

    assert subtrair(10, 5) == 5

def test_multiplicar():
    assert multiplicar(3, 4) == 12

    assert multiplicar(2, 0) == 0

def test_dividir():
    assert dividir(10, 2) == 5

    assert dividir(5, 2) == 2.5

def test_dividir_por_zero():
    with pytest.raises(ValueError): # pytest.raises verifica se uma exceção é lançada
        dividir(10, 0)