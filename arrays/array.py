import numpy as np
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
"""
#12.Escrever um programa que lê um vetor com 20 números inteiros e os imprime na tela. Troque, a seguir, o 1º elemento com o último, o 2º com o penúltimo etc., até o 10º com o 11º, e imprima o vetor modificado.
num = np.array([])
for i in range (20):
    n = int(input(f"Informe o {i+1}º número: "))
    num=np.append(num,n)
print(num)
for i in range(10):
    num[i], num[19-i] = num[19-i], num[i]
print(num)
"""
"""
#13.Numa eleição existem n candidatos identificados pelos números 1, 2, 3... n. Faça um programa que compute o resultado de uma eleição. Inicialmente, o programa deverá pedir o número total de candidatos e votantes. Em seguida, deverá pedir para cada votante votar (informando o número do candidato) e, ao final, imprimir o número de votos de cada candidato. Utilize um vetor para armazenar o total de votos de cada candidato.

tot_candidatos = int(input('Digite o total de candidatos: '))
tot_votantes = int(input('Digite o total de votantes: '))

num_votos = np.zeros(tot_candidatos + 1, dtype=int)
for i in range(tot_votantes):
    voto = int(input(f"Votante {i+1}, informe o número do candidato (1 a {tot_candidatos}): "))
    if 1 <= voto <= tot_candidatos:
        num_votos[voto] += 1
    else:
        print("Número de candidato inválido!")
print("\nResultado da eleição:")
for candidato in range(1, tot_candidatos + 1):
    print(f"Candidato {candidato}: {num_votos[candidato]} votos")
"""
"""
#14.Ler 100 números de matrículas de alunos e armazenar em um vetor. Esses números são distintos, ou seja, não existem números de matrículas iguais. Caso o usuário informe um número de matrícula que já existe, o programa deverá emitir um alerta.

total_matriculas = 100
matriculas = np.zeros(total_matriculas, dtype=int)

cont_matriculas = 0
while cont_matriculas < total_matriculas:
    matricula = int(input(f"Digite o número de matrícula do aluno {cont_matriculas + 1}: "))
    if matricula in matriculas:
        print("Matrícula já existe! Por favor, informe um número de matrícula diferente.")
    else:
        # Adiciona a matrícula ao vetor
        matriculas[cont_matriculas] = matricula
        cont_matriculas += 1
print("\nMatrículas cadastradas:")
print(matriculas)
"""
"""
#15.Faça um programa que leia um vetor com N elementos formado por valores do tipo inteiro. Crie então dois novos vetores, um com os valores pares e outro com os valores ímpares do vetor original.

N = int(input("Digite o número de elementos do vetor: "))
vetor_original = np.zeros(N, dtype=int)
for i in range(N):
    vetor_original[i] = int(input(f"Digite o valor do elemento {i+1}: "))

pares = []
impares = []

for valor in vetor_original:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

pares = np.array(pares)
impares = np.array(impares)

print("\nVetor original:", vetor_original)
print("Vetor de valores pares:", pares)
print("Vetor de valores ímpares:", impares)
"""
"""
#16.Faça um programa que:

#a) Leia um vetor A com N elementos já ordenados e um vetor B com M elementos também já ordenados.
#b) Intercale os dois vetores A e B, formando um vetor C, sendo que ao final do processo de intercalação, o vetor C continue ordenado. Nenhum outro processo de ordenação poderá ser utilizado além da intercalação dos vetores A e B.
#c) Caso um vetor (A ou B) termine antes do outro, o vetor C deverá ser preenchido com os elementos do vetor que ainda possui informações.

def intercalar_vetores(A, B):
    N = len(A)
    M = len(B)
    
    C = np.zeros(N + M, dtype=int)

    i, j, k = 0, 0, 0

    while i < N and j < M:
        if A[i] <= B[j]:
            C[k] = A[i]
            i += 1
        else:
            C[k] = B[j]
            j += 1
        k += 1

    while i < N:
        C[k] = A[i]
        i += 1
        k += 1

    while j < M:
        C[k] = B[j]
        j += 1
        k += 1

    return C

N = int(input("Digite o número de elementos do vetor A: "))
M = int(input("Digite o número de elementos do vetor B: "))

A = np.zeros(N, dtype=int)
print("\nDigite os elementos do vetor A (ordenados):")
for i in range(N):
    A[i] = int(input(f"Elemento {i+1}: "))

B = np.zeros(M, dtype=int)
print("\nDigite os elementos do vetor B (ordenados):")
for i in range(M):
    B[i] = int(input(f"Elemento {i+1}: "))

C = intercalar_vetores(A, B)

print("\nVetor A:", A)
print("Vetor B:", B)
print("Vetor C (intercalado):", C)
"""
"""
#17.Uma escola de samba recebeu como pontos pela alegoria os seguintes 5 valores inclusos no vetor Notas = [9.9, 9.7, 9.8, 10, 10]. Lembrando que a nota mais alta e a nota mais baixa são descartadas. Faça um programa que calcule a média final do quesito.
Notas = np.array([9.9, 9.7, 9.8, 10, 10])

nota_max = np.max(Notas)
nota_min = np.min(Notas)

Notas_sem_extremos = Notas[Notas != nota_max]
Notas_sem_extremos = np.append(Notas_sem_extremos, Notas[Notas == nota_max][1:]) 
Notas_sem_extremos = Notas_sem_extremos[Notas_sem_extremos != nota_min]
Notas_sem_extremos = np.append(Notas_sem_extremos, Notas[Notas == nota_min][1:])

media_final = np.mean(Notas_sem_extremos)

print(f"A média final do quesito, após descartar a nota mais alta e a mais baixa, é: {media_final:.2f}")
"""
















