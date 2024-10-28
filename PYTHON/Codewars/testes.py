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
"""
names = ['Peter']
def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return (f'{names[0]} like this')
    elif len(names) == 2:
        return (f'{names[0]} and {names[1]} like this')
    elif len(names) == 3:
        return (f'{names[0]}, {names[1]} and {names[2]} like this')
    else:
        return (f'{names[0]}, {names[1]} and {len(names)-2} others like this')
print(likes(names))
"""

st=str(input("digite uma string: "))

def is_pangram(st):#//verifica se uma string e um pangrama
    if len(st) < 26:#?verifica se a string tem mais de 26 letras
        return False
    st = st.lower()#?transforma a string em minuscula
    for i in range(97,123):#?a-z
        if chr(i) not in st:#?verifica se a letra não existe na string
            return False
    return True
print(is_pangram(st))