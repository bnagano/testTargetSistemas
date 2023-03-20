import math

numero = int(input("Digite um numero inteiro: "))

def quadradoPerfeito(x):
    numero = int(math.sqrt(x))
    return numero*numero == x

def fibonacci(numero):
    return quadradoPerfeito(5*numero*numero+4) or quadradoPerfeito(5*numero*numero-4)

if (fibonacci(numero) == True):
    print(f"{numero} é um número Fibonacci")
else:
    print (f"{numero} não é um número Fibonacci")