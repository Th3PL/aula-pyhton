def parImpar (numero) :
    if numero % 2 == 0:
        print("O número digitado é par")
    else:
        print("O número digitado é impar")

num = 1

print("Digite números inteiros, ao digitar 0 o programa finalizara")

while num != 0 :
    num = int(input())
    if num == 0:
        break
    
    parImpar(num)

