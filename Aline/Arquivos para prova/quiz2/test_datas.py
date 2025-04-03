import pytest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from datetime import datetime, timedelta
from datas import diferenca_datas

def test_diferenca_datas():
    data1 = datetime(2023, 1, 1) #(ANO, MES, DIA)
    data2 = datetime(2023, 1, 10)

    assert diferenca_datas(data1, data2, 'dias') == 9
    assert diferenca_datas(data1, data2, 'horas') == 216