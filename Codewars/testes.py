"""Testes de algoritmos."""
"""
def is_valid_walk(walk):
    
    #Returns True if the walk will take exactly 10 minutes and return to the starting point.
    # Initialize counters for each direction
    north_south = 0
    east_west = 0
    
    # Iterate over each direction in the walk
    for direction in walk:
        if direction == 'n':
            north_south += 1
        elif direction == 's':
            north_south -= 1
        elif direction == 'e':
            east_west += 1
        elif direction == 'w':
            east_west -= 1
    
    # Check if the walk takes exactly 10 minutes and returns to the starting point
    return len(walk) == 10 and north_south == 0 and east_west == 0
"""
"""
n=int(input("Digite um número: "))
def row_sum_odd_numbers(n):
    
    piramide = []
    num = 1
    for i in range(n):
        linha = []#cria uma linha
        for j in range(i+1):#cria uma coluna
            linha.append(num)#adiciona o valor
            num += 2#adiciona 2 ao valor
        piramide.append(linha)#adiciona a linha
    return sum(piramide[-1])
print(row_sum_odd_numbers(n))
"""

