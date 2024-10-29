#NOTE:1. Descreva os custos e benefícios de definir e utilizar uma função recursiva.
#INFO:O custo de utilizar uma função recursiva é o uso de memória ram, visto que  cada chamada da função cria uma nova instância da função, e o benefício é a simplicidade  e a clareza do código, pois a recursividade permite que o problema seja resolvido  de forma mais natural e intuitiva.


#NOTE:2. Explique o que acontece quando a seguinte função recursiva é chamada com o valor 4 como argumento:

#INFO:vai contar de 4 até 1 , e vai imprimir cada número, e vai continuar até que o valor seja 1, e quando chegar a 0 ela para.

def example(n):

       if n > 0:

           print(n)

           example(n - 1)
print(example(4))



#NOTE:3. Explique o que acontece quando a seguinte função recursiva é chamada com o valor 4 como argumento:
#INFO:Vai contar o valor de 4 até 0 e quando chegar em -1 ele vai parar.

def example(n):

    if n > 0:

        print(n)

        example(n)

    else:

        example(n - 1)

 
#NOTE:4. Uma função é recursiva quando ela atende as seguintes leis:

#NOTE:1.Um algoritmo recursivo deve ter um caso básico 
#NOTE:2.Um algoritmo recursivo deve mudar o seu estado e se aproximar do caso básico.
#NOTE:3.Um algoritmo recursivo deve chamar a si mesmo, recursivamente.
       #NOTE:Descreva cada uma das leis acima e apresente exemplos.

def example(n):

    if n > 0:#INFO:1. Caso  básico, quando n é maior que 0, a função imprime o valor de n e

        print(n)

        example(n)
    else:

        example(n - 1)#INFO:2&3. Chama a função recursiva se modifica e se aproxima  o caso básico a cada chamada.