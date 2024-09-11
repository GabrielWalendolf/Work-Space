import numpy as np #usar np para chamar a codificação de numpy
import array as arr
"""
#1.Faça um programa que possua um vetor denominado A que armazene 6 números inteiros. O programa deve executar os seguintes passos:

A = np.array([])#a
A[0]=1
A[1]=0
A[2]=5
A[3]=-2
A[4]=-5
A[5]=7

soma=A[0]+A[1]+A[5] #b 
print(soma)

A[4]=100#c

for i in range(6):#d
    print (A[i])
    i+=1
"""
"""
#2.Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos.
num = np.array([])
for i in range (6):
    numero = int(input("Informe um número: "))
    num=np.append(num,numero)
print(num)
"""
"""
#3.Ler um conjunto de números reais, armazenando-o em um vetor e calcular o quadrado das componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos têm 10 elementos cada. Imprimir todos os conjuntos.

vetor = np.array([])

for i in range(10):
    numeral = float((input("Informe um número real: ")))
    vetor = np.append(vetor, numeral)
    vetorquad = vetor**2
print(vetor)
print(vetorquad)
"""
"""
#4.Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos.
num = np.array([])
for i in range (8):
    numero = int(input("Informe um número: "))
    num=np.append(num,numero)
print(num)
x= int(input("informe a posição: "))-1
while x <=-1 or x>=8:
    x= int(input("informe a posição: "))-1
y= int(input("Informe uma outra posição: "))-1
while y <=-1 or x>=8:
    y= int(input("Informe uma outra posição: "))-1
print(num[x])
print(num[y])
"""
"""
#5.Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui.
vetor = np.zeros(10, dtype=int)

for i in range(10):
    vetor[i] = int(input(f"Digite o valor da posição {i + 1}: "))

indices_pares = np.where(vetor % 2 == 0)[0]  

print(f"Indices dos números pares: {indices_pares}")
print(f"Números pares encontrados: {vetor[indices_pares]}")
"""
"""
#6.Faça um programa que receba do usuário um vetor com 10 posições. Em seguida deverá ser impresso o maior e o menor elemento do vetor.
num = np.array([])

menor=0
maior=0

for i in range (10):
    n = int(input("Informe um número: "))
    if maior == 0:
        maior = n
    if menor == 0:
        menor = n
    
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    num=np.append(num,n)
print(menor)
print(maior)
"""

























