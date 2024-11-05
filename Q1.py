#  Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 
#   valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que 
#   desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando 
#   se o número informado pertence ou não a sequência.
# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou 
#   pode ser previamente definido no código;

fib = []
fib.append(0)
fib.append(1)

X = 377

while True:
    fib.append(fib[-1]+fib[-2])

    print(fib)
    print("\n")

    # Se o número estiver na lista
    if X in fib:
        print(f"\n\n${X} está na lista.")
        break

    # Se o número atual(última posição da lista) for maior que o número desejado e não estiver na lista
    if X < fib[-1]:
        print(f"\n\n!!! ${X} não está na lista. !!!")
        break


    



    