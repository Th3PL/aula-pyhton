import random

#difinindo variaveis
palavras = ["lagartixa", "nostalgia", "crocodilo"]
sorte = random.choice(palavras)
tentativas = 0
tentativasmax = 5

#possibilidades de dicas
if sorte == "lagartixa":
    dica = ("come aranhas é um réptil e um vive na casa das pessoas")
if sorte == "nostalgia":
    dica = ("Felipe castanhari, canal ?")
if sorte == "crocodilo":
    dica = ("qual animal é o símbolo da lacoste?")

#essa lista cria o mesmo numero de elementos da palavra sorteada
vazio = ["_"]

#loop de repetição de erros e acertos no jogo
while "_" in vazio and tentativas < tentativasmax:
    print("Bem vindo ao jogo da forca!!")
    print(f"Dica: {dica}")
    print("|====|===")
    print("|    |")
    if tentativas > 0:
        print("|    O")
    if tentativas > 1:
        print("|   / /")
        if tentativas == 2:
            print()
        if tentativas > 2:
            print("|    ||")
            if tentativas == 3:
                print()
            if tentativas > 3:
                print("|    ~~")
                if tentativas == 4:
                    print()
    print("|")
    print("|")
    print(vazio)

    #passando letras maiusculas para minusculas
    letra = input("Digite uma letra: ").lower()

    #validação de letras na lista
    if letra in sorte:
        for i in range(len(sorte)):
            if sorte[i] == letra:
                vazio[i] = letra
    else:
        print()
        print(f"A palavra não tem a letra {letra}")
        print()
        tentativas += 1

#validação se o jogo continua ou não
if "_" not in vazio:
    print("Parabéns! Você adivinhou a palavra:", sorte)
else:
    print("Você perdeu! A palavra era:", sorte)
