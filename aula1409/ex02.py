try:
    print("Digite outro ditado popular : ")
    escrito = input()
    f = open('d:/ex01.txt', 'a', encoding='UTF-8')
    f.write('\n' + escrito)
    f.close()
    print("Arquivo Completo : ")
    f = open('d:/ex01.txt', 'r', encoding='UTF-8')
    print(f.read())
    f.close()

except FileNotFoundError:
    print("Caminho e/ou arquivo inexistente")
