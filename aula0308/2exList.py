import statistics
numeros = []
num = media = soma =0.0

for i in range(0,2,1):
    print("Digite um numero real: ")
    num = float(input())
    soma += num 
    numeros.append(num)

#media = soma / len(numeros)

media = statistics.mean(numeros)

print(f"A média dos numeros é {media}")