import pytest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from ordenacao import ordenar_crescente, ordenar_decrescente

def test_ordenar_crescente():
    assert ordenar_crescente([3, 1, 4, 2]) == [1, 2, 3, 4]

    assert ordenar_crescente(['d', 'b', 'a', 'c']) == ['a', 'b', 'c', 'd'] # NÃO ESQUECER DAS ASPAS!!!!!!

def test_ordenar_decrescente():
    assert ordenar_decrescente([2, 1, 3, 4]) == [4, 3, 2, 1]

    assert ordenar_decrescente(['a', 'd', 'b', 'c']) == ['d', 'c', 'b', 'a']
