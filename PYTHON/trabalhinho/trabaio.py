lista = [22, 4, 50, 24, 72, 17, 12, 97, 77, 13, 34, 96, 81, 14, 5, 31, 54, 46, 12, 77, 93, 43, 10, 72, 2, 88, 68, 32, 97, 65, 65, 2]

def organizar(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):  # j vai até n-i-1 para evitar verificar índices já ordenados
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]  # troca os elementos se estão na ordem errada
    return lista

print(organizar(lista))
