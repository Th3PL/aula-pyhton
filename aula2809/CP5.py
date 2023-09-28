# Pedro Lucas     rm: 550366
# Pedro Henrique  rm:98608
# Victor Nuzzi    rm:98209
# Lucca vilaça    rm:551538



import random
import csv

# Abre o arquivo com a roda e com as palavras
roda_valores = []
with open('d:/roleta.txt', 'r') as roda_file:
    roda_valores = roda_file.read().splitlines()

with open('d:/palavras.csv', 'r') as palavras_file:
    reader = csv.reader(palavras_file)
    palavras = next(reader)

# Sorteia as palavras do jogo
palavras_aleatorias = random.sample(palavras, 3)
dica = "Jogos"

# Coloca o nome dos jogadores
jogadores = []
for i in range(3):
    jogador = input(f"Digite o nome do jogador {i + 1}: ")
    jogadores.append({'nome': jogador, 'reais': 0})

letras_adivinhadas = []
jogador_atual = 0
rodadas = 0
progresso_palavras = [0] * len(jogadores)
letras_necessarias = set()

# Inicializa o conjunto de letras necessárias
for palavra in palavras_aleatorias:
    letras_necessarias.update(set(palavra))

# Exibe a dica apenas no início
print(f"Dica: {dica}")

# Escolhe o jogador e inicia o jogo
while True:
    jogador = jogadores[jogador_atual]
    print(f"\nVez de {jogador['nome']}")
    input("Pressione Enter para rodar a roda...")

    opcao_roda = random.choice(roda_valores)
    print(f"A roda parou em: {opcao_roda}")

    if opcao_roda == 'pt':
        print(f"{jogador['nome']} perdeu tudo!")
        jogador['reais'] = 0
    elif opcao_roda == 'pv':
        print(f"{jogador['nome']} passou a vez.")

        # Escolhe letra
    else:
        letra = input("Escolha uma letra: ").lower()
        if len(letra) == 1 and letra.isalpha():
            if letra in letras_adivinhadas:
                print("Você já adivinhou essa letra antes.")
            else:
                acertos = 0
                for i, palavra in enumerate(palavras_aleatorias):
                    if letra in palavra:
                        acertos += palavra.count(letra)
                        dica = "".join([letra if letra in palavra or dica_letra == letra else "_" for dica_letra in dica])
                        progresso_palavras[jogador_atual] += palavra.count(letra)
                jogador['reais'] += float(opcao_roda) * acertos
                if acertos > 0:
                    letras_adivinhadas.append(letra)
                print(f"Letra correta! {jogador['nome']} ganhou R${opcao_roda} x {acertos}.")
                letras_restantes = letras_necessarias - set(letras_adivinhadas)
                letras_restantes = [letra for letra in letras_restantes if letra.isalpha()]
                if len(letras_restantes) == 0:
                    print(f"Todas as letras únicas foram adivinhadas!")
                    premio_multiplicador = 1
                    for palavra in palavras_aleatorias:
                        premio_multiplicador *= palavra.count(letra)
                    jogador['reais'] *= premio_multiplicador
                    print(f"{jogador['nome']} venceu o jogo com R${jogador['reais']:.2f}.")
                    break
                elif any(len(palavra) - progresso_palavras[jogador_atual] == 3 for palavra in palavras_aleatorias):
                    palavra_a_adivinhar = [palavra for palavra in palavras_aleatorias if len(palavra) - progresso_palavras[jogador_atual] == 3][0]

                    # Deixando o jogador chutar a palavra
                    resposta = input("Você quer tentar adivinhar a palavra com 3 letras faltando? (S/N): ").strip().lower()
                    if resposta == 's':
                        tentativa = input(f"Digite sua tentativa para a palavra: ").strip().lower()
                        if tentativa == palavra_a_adivinhar:
                            print(f"Palavra correta! {jogador['nome']} ganhou o jogo com R${jogador['reais']:.2f}.")
                            break
                        else:
                            print("Tentativa incorreta. Continue jogando.")
        else:
            print("Escolha uma letra válida.")

    print("\nLetras adivinhadas:", ', '.join(letras_adivinhadas))
    for jogador in jogadores:
        print(f"{jogador['nome']}: R${jogador['reais']:.2f}")

    jogador_atual = (jogador_atual + 1) % 3
    
    if jogador_atual == 0:
        rodadas += 1
        print(f"\nRodada {rodadas} concluída.")
