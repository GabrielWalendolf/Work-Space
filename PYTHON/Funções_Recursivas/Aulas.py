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
"""
#INFO:Crie um programa, que contenha uma função recursiva que receba dois inteiros positivos k e n e calcule kn. Utilize apenas multiplicações. O programa principal deve solicitar ao usuário os valores de k e n e imprimir o resultado da chamada da função.

k=int(input('Digite um número inteiro'))
n=int(input('Digite o expoente'))
def potencia (k,n):
    if n == 0:
        return 1
    elif n == 1:
        return k
    else:
        return k * potencia(k,n-1)
print(potencia(k,n))
"""
"""
#INFO:Faça uma função recursiva que permita inverter um número inteiro N. Ex: 123 - 321
def inverter(n,b=0):
    # Caso base: se n for 0, retorna 0
    if n == 0:
        return b
    else:
        b=b*10+n%10 # Adiciona o último dígito do número invertido
        return (inverter(n // 10, b)) # Chama a função recursivamente com o número reduzido

# Solicita ao usuário um número inteiro
n = int(input('Digite um número para ser invertido: '))
# Chama a função e imprime o resultado
print(inverter(n))
"""
"""
#INFO:Faça uma função recursiva que permita somar os elementos de um vetor de inteiros
n=[1,2,5,3,4]

def soma_vetor(n):
    if len(n) == len(n)-len(n):
        return len(n)
    else:
        return n[0] + soma_vetor(n[1:])
print(soma_vetor(n))
"""
"""
#INFO:Crie um programa em C que receba um vetor de números reais com 100 elementos. Escreva uma função recursiva que inverta ordem dos elementos presentes no vetor.
n=[1,2,3,4,4,5,5,6,673,5]

def inverter_vetor(n):
    if len(n) == 1:
        return n
    else:
        return [n[-1]] + inverter_vetor(n[:-1])
print(inverter_vetor(n))
"""
"""
#NOTE:1. Descreva os custos e benefícios de definir e utilizar uma função recursiva.
#INFO:O custo de utilizar uma função recursiva é o uso de memória ram, visto que  cada chamada da função cria uma nova instância da função, e o benefício é a simplicidade  e a clareza do código, pois a recursividade permite que o problema seja resolvido  de forma mais natural e intuitiva.


#NOTE:2. Explique o que acontece quando a seguinte função recursiva é chamada com o valor 4 como argumento:

#INFO:vai contar de 4 até 1 , e vai imprimir cada número, e vai continuar até que o valor seja 1, e quando chegar a 0 ela para.

def example(n):

       if n > 0:

           print(n)

           example(n - 1)
print(example(4))



#NOTE:3. Explique o que acontece quando a seguinte função recursiva é chamada com o valor 4 como argumento:
#INFO:Vai contar o valor de 4 até 0 e quando chegar em -1 ele vai parar.

def example(n):

    if n > 0:

        print(n)

        example(n)

    else:

        example(n - 1)

 
#NOTE:4. Uma função é recursiva quando ela atende as seguintes leis:

#NOTE:1.Um algoritmo recursivo deve ter um caso básico 
#NOTE:2.Um algoritmo recursivo deve mudar o seu estado e se aproximar do caso básico.
#NOTE:3.Um algoritmo recursivo deve chamar a si mesmo, recursivamente.
       #NOTE:Descreva cada uma das leis acima e apresente exemplos.

def example(n):

    if n > 0:#INFO:1. Caso  básico, quando n é maior que 0, a função imprime o valor de n e

        print(n)

        example(n)
    else:

        example(n - 1)#INFO:2&3. Chama a função recursiva se modifica e se aproxima  o caso básico a cada chamada.
"""








