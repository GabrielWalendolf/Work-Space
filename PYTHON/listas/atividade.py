"""
#Faça um programa que dada a matriz, gere a matriz oposta a matriz oposta possui valores que se somados a matriz original gera uma matriz com valores zerados.

A=[[2,-3],[-1,4]]

#oposta = [[-x for x in linha] for linha in A]

oposta = []
for linha in A:
    oposta.append([-x for x in linha])

print(oposta)
"""
"""
# Faça um programa para ler e imprimir uma matriz 2x4 de números inteiros.

mat = [[0,0,0,0],[0,0,0,0]]
for i in range(2):
    for j in range(4):
        a = int(input("digite um valor: "))
        mat[i][j]=a

print(mat)
"""
"""
#A matriz identidade é matriz quadrada de ordem N (2x2, 3x3, 4x4, ... NXN) em que os elementos da diagonal principal são 1 e os outros elementos são 0. Faça um programa que peça ao usuário informar o tamanho da ordem e gere a matriz identidade.

#Exemplo de matriz identidade de ordem 3x3
# 1 0 0
# 0 1 0
# 0 0 1

ordem = int(input("Informe a ordem da matriz identidade: "))
mat = [[0 for i in range(ordem)] for j in range(ordem)]

for i in range(ordem):
    for j in range(ordem):
        if i == j:
            mat[i][j] = 1
        else:
            mat[i][j] = 0

print(mat)
"""
"""
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
"""
"""
#3.Dada as matrizes A e B, determine A + B.
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
"""



