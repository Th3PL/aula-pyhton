def maior(numeros) :
    numeros.sort(reverse = True)
    for i in numeros:
        print(f"{i:.3f}")

num = []
print("Digite quatro números inteiros")
for i in range(0,4,1):
    valor = float(input())
    num.append(valor)
    
maior(num)

