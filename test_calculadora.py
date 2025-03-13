import pytest
from calculadora import soma, divisao

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, -1) == -2
    assert soma(0, 0) == 0

def test_divisao():
    assert divisao (10, 2) == 5
    assert divisao (9, 3) == 3

def test_division_por_zero():
    with pytest.raises(ValueError, match="Não é permitido a divisão por zero!"):
        divisao(10, 0)