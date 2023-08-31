import random

matriz  = []
soma1 = 0.0

#gerando matriz
for i in range(0, 5, 1):
    linha = []
    for j in range(0, 5, 1):
        valor = float(random.randrange(10,20))
        linha.append(valor)
    matriz.append(linha[:])
for i in matriz:
    print(i)

for i in range(0, 5, 1):
    for j in range(0, 5, 1):
        soma1+= matriz[i][j]
       

print(f"Soma 1: {soma1}")