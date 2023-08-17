carta = dict(nome = "Cell", KI = 7400, tecnicas = 6000, velocidade = 66, transformacoes = 3)
print("Escreva uma nova caracteristica para sua carta:")
print(f"Nome: ")
nome = input()
print(f"Valor: ")
valor = int(input())
carta.update({nome : valor})

print("Escolha dentre as seguintes caracteristicas:")
for i in carta.keys():
    print(i)

escolha = input()
print(carta[escolha])