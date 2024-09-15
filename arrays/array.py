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
"""
#7.Escreva um programa que leia 10 números inteiros e os armazene em um vetor. Imprima o vetor, o maior elemento e a posição que ele se encontra.
num = np.array([])
maior=0
for i in range (10):
    n = int(input(f"Informe um número {i+1}: "))
    if maior == 0:
        maior = n
    if n > maior:
        maior = n
    num=np.append(num,n)
    pos = np.where(num == maior)[0]
print("Vetor:", num)
print("Maior número:", maior)
print("Posição do maior número:", pos)
"""
"""
#8.Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos na ordem inversa.
num = np.array([])
for i in range (6):
    n = int(input(f"Informe um número {i+1}: "))
    num=np.append(num,n)
num = num[::-1]
print(num)
"""
"""
#9.Crie um programa que lê 6 valores inteiros pares e, em seguida, mostre na tela os valores lidos na ordem inversa.

num = np.array([])
for i in range (6):
    n = int(input(f"Informe um número par{i+1}: "))
    if n % 2 != 0:
        n = int(input("digite um número par: "))
        if n % 2 == 0:
            num=np.append(num,n)
    elif n % 2 == 0:
        num=np.append(num,n)
num = num[::-1]
print(num)
"""
"""
#10.Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule e imprima a média geral.
num = np.array([])
media= 0
for i in range (15):
    n = int(input(f"Informe a nota do aluno {i+1}: "))
    num=np.append(num,n)
    media += num[i]
media=media/15
print(media)
"""
"""
#11.Faça um programa que preencha um vetor com 10 números reais, calcule e mostre a quantidade de números negativos e a soma dos números positivos desse vetor.
num = np.array([float(input(f"Informe o {i+1}º número: ")) for i in range(10)])
n=num[num<0]
p=num[num>0]
negativos=len(n)
positivos=np.sum(p)
print(f"Quantidade de números negativos {negativos}")
print(f"A soma dos números positivos {positivos}")
"""

#12.Escrever um programa que lê um vetor com 20 números inteiros e os imprime na tela. Troque, a seguir, o 1º elemento com o último, o 2º com o penúltimo etc., até o 10º com o 11º, e imprima o vetor modificado.

num = np.array([int(input(f"Informe o {i+1}º número: ")) for i in range(20)])
num1=[]
for i in range (10):
    num1[i]=num[i]
 
















