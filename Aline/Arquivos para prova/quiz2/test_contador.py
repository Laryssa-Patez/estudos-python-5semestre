import pytest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from contador import contador_palavras

def test_contador():
    assert contador_palavras("Olá, mundo!") == 2

    assert contador_palavras("") == 0

    assert contador_palavras("Palavra1, palavra2") == 2

    assert contador_palavras("    Espaço     extra      ") == 2

    assert contador_palavras("palavra palavra repetida") == 3