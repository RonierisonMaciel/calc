import pytest
from calculadora import soma, divisao, multiplicacao, subtracao, square


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


def test_multiplicacao():
    assert multiplicacao(2, 3) == 6
    assert multiplicacao(0, 0) == 0
    assert multiplicacao(1, 1) == 1


def test_subtracao():
    assert subtracao(2, 3) == -1
    assert subtracao(0, 0) == 0
    assert subtracao(1, 1) == 0


def test_square():
    assert square(2) == 4
    assert square(1) == 1
    assert square(-2) == 4