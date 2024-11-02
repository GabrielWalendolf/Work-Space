
#NOTE:-8- O máximo divisor comum dos inteiros x e y é o maior inteiro que é divisível por x e  y. Escreva uma função recursiva mdc em python, que retorna o máximo divisor comum de x e y. O mdc de x e y é definido como segue: se y é igual a 0, então mdc(x,y) é x; caso contrário, mdc(x,y) é mdc (y, x%y), onde % é o operador resto.
"""
x=int(input('digite um número inteiro: '))
y=int(input('digite outro número inteiro: '))
def mdc(x,y):
 if y == 0:
  return x
 else:
  return mdc(y, x%y)
print(mdc(x,y))
"""
#NOTE:-9- Crie  uma  função  recursiva  que  receba  um  número  inteiro  positivo  N  e  calcule  o somatório dos números de 1 a N.
"""
n=int(input('digite um número inteiro: '))
def soma(n):
    if n == 1:
        return 1
    else:
        return n + soma(n-1)
print(soma(n))
"""

#NOTE:-10- Escreva  uma  função  recursiva  que  determine  quantas  vezes  um  dígito  K  ocorre em um número natural N. Por exemplo, o dígito 2 ocorre 3 vezes em 762021192.
"""
k=int(input('digite um número inteiro: '))
n=int(input('digite outro número inteiro: '))
def  ocorrencia(k,n):
    if n == 0:
        return 0
    else:
        if n%10 ==k:
            return 1 + ocorrencia(k,n//10)#// faz uma divisão inteira e arredonda para baixo
        else:
            return ocorrencia(k,n//10)
print(ocorrencia(k,n))
"""
#NOTE:A multiplicação de dois números inteiros pode ser feita através de somas sucessivas. Proponha um algoritmo recursivo Multip_Rec(n1,n2) que calcule a multiplicação de dois inteiros.
"""
n1=int(input('digite um número inteiro: '))
n2=int(input('digite outro número inteiro: '))
def  Multip_Rec(n1,n2):
  if n2 == 0:
    return 0
  else:
    return n1 + Multip_Rec(n1,n2-1)
print(Multip_Rec(n1,n2))
"""
#NOTE:Faça  uma  função  recursiva  que  receba  um  número  inteiro  positivo  N  e  imprima todos os números naturais de 0 até N em ordem crescente.
"""
n=int(input('Digite um número inteiro: '))
def  imprime(n,x=0):
  if n == 0:
    return x
  else:
    return x,imprime(n-1,x+1)
print(imprime(n))
"""







