# função soma	
def soma(a, b):
    return a + b

# função divisão
def divisao(a, b):
    if b == 0:
        raise ValueError("Não é permitido a divisão por zero!")
    return a / b

# função multiplicação
def multiplicacao(a, b):
    return a * b

# função subtração
def subtracao(a, b):
    return a - b

# função square
def square(a):
    return a * a