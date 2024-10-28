#aula 1
"""
#exemplo de função recursiva utilizando fatorial
#funções recursivas tem que ter obrigatóriamente um caso base e um caso recursivo. Caso o caso base seja executado, o caso recursivo não será executado.
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

print(fatorial(5))
"""
"""
#exemplo de função recursiva utilizando fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))
"""
"""
#exemplo de função recursiva utilizando soma
def soma(n):
    if n == 1:
        return 1
    else:
        return n + soma(n-1)

print(soma(5))
"""