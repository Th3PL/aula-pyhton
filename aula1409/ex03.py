digitados = {0}
print("Digite números interos, ao digitar 0 o programa irá parar ")
digitado = int(input('Valor: '))
while (digitado != 0):
    try:
        digitados.add(digitado)
        digitado = int(input('Valor: '))
    except ValueError:
        print("Valor inválido, tente novamente: ")
        digitado = int(input('Valor: '))

digitados.remove(0)
try:
    f = open('d:/ex03.txt', 'a', encoding='UTF-8')
    for i in digitados:
        if i % 2 == 0:
            f.write(str(i) + ' ')
            f.close
    print("Números pares digitados:")
    f = open('d:/ex03.txt', 'r', encoding='UTF-8')
    print(f.read())
    f.close()
except FileNotFoundError:
    print("Caminho e/ou arquivo inexistente")
