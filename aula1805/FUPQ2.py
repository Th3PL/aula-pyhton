import math

def raiz(n) :
    result = math.sqrt(n) 
    return result

print("Digite um número inteiro: ")
num = int(input())
digitado = num

resultado = raiz(num)

print(f'A raiz do número {digitado} é {int(resultado)}')
