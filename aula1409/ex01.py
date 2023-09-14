try:
    print("Digite um ditado popular: ")
    escrito = input()
    f = open('d:/ex01.txt', 'w', encoding='UTF-8')
    f.write(escrito)
    f.close
    print("Ditado escrito: ")
    f = open('d:/ex01.txt', 'r', encoding='UTF-8')
    print(f.read())
    f.close()
except FileNotFoundError:
    print("Caminho e/ou arquivo inexistente")
