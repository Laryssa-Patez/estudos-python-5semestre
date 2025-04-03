import pytest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from validador_email import validar_email

def test_emails_validos():
    assert validar_email("usuario@exemplo.com") == True
    
    assert validar_email("nome.sobrenome@dominio.com.br") == True

    assert validar_email("user+tag@exemplo.com") == True

    assert validar_email("a@b.com") is True  # Email mínimo válido

def test_emails_invalidos():
    assert validar_email("usuario@") == False

    assert validar_email("@dominio.com") == False

    assert validar_email("usuario.dominio.com") == False
    
    assert validar_email("usuario@dominio") == False

    assert validar_email("usuário@dominio.com") == False

    assert validar_email("with space@dom.com") == False
    
    assert validar_email("no@tld") == False