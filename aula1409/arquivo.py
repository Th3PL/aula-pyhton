try:
    f = open('d:/test.txt', 'w', encoding='UTF-8')
    f.write('\nSou pequenininha')
    f.write('\nDo tamanho de um botão')
    f.close
    f = open('d:/test.txt', 'r', encoding='UTF-8')
    # for x in f:
    #     print(x)
    # f.close()
    print(f.read())
    f.close()
except FileNotFoundError:
    print("Caminho e/ou arquivo inexistente")
