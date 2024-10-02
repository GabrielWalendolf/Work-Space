# Listas
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

#3





