import pytest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from telefone import validar_telefone

def test_validar_telefone():
    assert validar_telefone("(14) 99876-5544") == True

    assert validar_telefone("(11) 36780-8945") == True

    assert validar_telefone("11 987654332") == False

    assert validar_telefone("(14) 9876-76") == False

    assert validar_telefone("(789) 98767-8765") == False