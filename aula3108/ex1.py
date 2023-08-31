#Aluno: Pedro Lucas de Andrade Nunes 550366

import random
matriz=[]
somaL4 = 0
somaC2 = 0
somaDP = 0
somaDC = 0
somaTodos = 0

#gerando matriz
for i in range(0, 5, 1):
    linha = []
    for j in range(0, 5, 1):
        valor = random.randrange(10,30)
        linha.append(valor)
    matriz.append(linha[:])
for i in matriz:
    print(i)
#soma linha 4
for i in range(0, 5, 1):
    somaL4+=matriz[3][i]     
print(f"Soma linha 4 = {somaL4}")
#soma coluna 2
for i in range(0, 5, 1):
    somaC2+=matriz[i][1]
print(f"Soma Coluna 2 = {somaC2}")
#soma diagonal principal
for i in range(len(matriz)):
    somaDP+= matriz[i][i]
print(f"Soma Diagona principal = {somaDP}")
#soma diagonal secundária
for i in range(len(matriz)):
    somaDC+= matriz[i][len(matriz)-i-1]
print(f"Soma Diagona secundária = {somaDC}")
#Somando todos os valores
for i in range(0, 5, 1):
    for j in range(0, 5, 1):
        somaTodos+= matriz[i][j]
print(f"Soma de todos os valores da matriz = {somaTodos}")