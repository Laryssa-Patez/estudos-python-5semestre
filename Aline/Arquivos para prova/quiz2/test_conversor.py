import pytest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

#OBRIGATÓRIA ESSAS 4 PRIMEIRAS!!!! 

from conversor import dolar_para_euro, real_para_dolar

def test_dolar_para_euro():
    assert dolar_para_euro(100) == 85 # Verifica se 100 dólares convertem para 85 euros

    assert dolar_para_euro(0) == 0  # Verifica se 0 dólares convertem para 0 euros

def test_real_para_dolar():
    assert real_para_dolar(100) == 19  # Verifica se 100 reais convertem para 19 dólares

    assert real_para_dolar(50) == 9.5 # Verifica se 50 reais convertem para 9.5 dólares
