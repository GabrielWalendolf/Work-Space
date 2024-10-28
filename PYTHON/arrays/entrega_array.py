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