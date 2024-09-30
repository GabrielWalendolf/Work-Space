"""
## Listas
# Listas sao conjuntos ordenados de elementos, podem ser compostos por qualquer tipo de dado,
# incluindo strings, numeros, booleanos, outras listas, etc. As listas sao mutaveis, ou seja,
# podem ser alteradas apos sua criacao.

# Criacao de listas
# Listas podem ser criadas de duas maneiras, com colchetes ou com a funcao list()
lista1 = [1, 4, 7, 8]
lista2 = list((1, 4, 7, 8))

# Metodos de listas
# copy(): copia a lista atual e torna ela nao editavel caso a lista copiada seja alterada
lista3 = lista1.copy()

# append(): adiciona um elemento na lista
lista1.append(9)

# insert(): insere um elemento na posicao desejada
lista1.insert(2,90)

# remove(): remove um elemento da lista
lista1.remove(90)

# pop(): remove um elemento da posicao desejada
lista1.pop(2)

# clear(): limpa a lista
lista1.clear()

# extend(): adiciona uma lista na lista
lista1.extend([1,2,3])

# index(): retorna o indice do elemento na lista
print(lista1.index(4))

# count(): retorna o numero de vezes que o elemento aparece na lista
print(lista1.count(4))

# sort(): ordena a lista em ordem crescente
lista1.sort()

# reverse(): ordena a lista em ordem decrescente
lista1.reverse()

# len(): retorna o tamanho da lista
print(len(lista1))

# in: verifica se um elemento esta na lista
print(4 in lista1)
"""
"""
## Matrizes
# Matrizes sao listas de listas, onde cada item da lista e uma lista em si, que pode ser acessada atraves de um par de indices.
# Apenas as listas podem ser usadas como matrizes, outros tipos de dados como strings e tuplas nao podem.

# Criacao de matrizes
# Matrizes podem ser criadas de forma explicita, ou atraves de uma lista de listas.
matriz1 = [[1,2,3], [4,5,6], [7,8,9]]
matriz2 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

# Acessando elementos de uma matriz
# Podemos acessar um elemento de uma matriz atraves de dois indices, um para a linha e outro para a coluna
print(matriz1[1][2]) # imprime 6

# Metodos de matrizes
# Apenas as listas tem metodos, matrizes nao tem metodos proprios.
"""

#Exercicio dia 30/09/2024
#1.Faça um programa para ler e imprimir uma matriz 2 × 4 de números inteiros.
mat_2x4=[[1,2,3,4],[5,6,7,8]]
print(mat_2x4)
#2.Dada a seguinte matriz, calcule:

#1   2   3   4  
#5   6   7   8  
#9   10  11  12  
#13  14  15  16

#2.i. A soma dos elementos da primeira coluna;
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
soma=0
for i in range(4):
    soma+=mat[0][i]
print(soma)
#2.ii. O produto dos elementos da primeira linha;
prod=1
for i in range(4):
    prod*=mat[i][0]
print(prod)
#2.iii. A soma de todos os elementos;
soma_all=0
for i in range(4):
    for j in range(4):
        soma_all+=mat[i][j]
print(soma_all)
#2.iv. O produto da diagonal principal.
prod_diag=1
for i in range(4):
    prod_diag*=mat[i][i]
print(prod_diag)

#Dada as matrizes A e B, determine A + B.
#A = [-10  1  4  6]  
#    [2   3  2  8]  

#B = [1   8   4  -1]  
#    [0   6   3  -3]

a=[[-10,1,4,6],[2,3,2,8]]
b=[[1,8,4,-1],[0,6,3,-3]]

c=[[0,0,0,0],[0,0,0,0]]
for i in range(2):
    for j in range(4):
        c[i][j]=a[i][j]+b[i][j]
print(c)






