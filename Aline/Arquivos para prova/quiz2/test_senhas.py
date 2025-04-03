import pytest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from senhas import senha_segura

def test_senha_segura():
    assert senha_segura("Senha123@") == True

    assert senha_segura("senhafraca") == False

    assert senha_segura("SENHAFORTE") == False

    assert senha_segura("senha123") == False