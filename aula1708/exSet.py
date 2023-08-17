#Aluno Pedro Lucas de Andrade Nunes RM: 550366

valores = {0}
print("Você deseja uma lista de números reais ou inteiros: ")
tipo = input().upper()
valores.clear()

if tipo.upper() == "INTEIRO":
    while len(valores) < 10:
        print(f"Digite um número do tipo {tipo}")
        digitado = int(input())
        valores.add(digitado)
else:
    while len(valores) < 10:
        print(f"Digite um número do tipo {tipo}")
        digitad = float(input())
        valores.add(digitad)

maiorDigitado = 0
for i in valores:
    if i > maiorDigitado:
        maiorDigitado = i

print(f"Tipo escolhido: {tipo} \nMaior valor na Lista: {maiorDigitado} \nTamando da lista: {len(valores)}")
print(f"Lista completa: {valores}")