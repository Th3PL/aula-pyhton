# Pedro Lucas     rm: 550366
# Pedro Henrique  rm:98608
# Victor Nuzzi    rm:98209
# Lucca vilaça    rm:551538


import random 
import csv
import re
from time import sleep

roleta = []
jogadores = []
saldos = [0, 0, 0]
letras = []
letras_excluidas = []

jogadas_rodada = cont = cont1 = cont2 = cont3 = rodada = acertou = novo_saldo = roleta_rodada = acertos = letra_verificacao = 0

# Abrindo o arquivo da roleta 
ft = open('d:/roleta.txt', 'r', encoding='UTF-8')
for i in range(0, 12, 1):
    linha = ft.readline()  
    roleta.append(linha)  
ft.close()

# Adicionar _ no tamanho das palavras
fp = open('d:/palavras.csv', 'r', encoding='UTF-8')
palavras = csv.reader(fp)
for ps in palavras:
    for p in ps:
        letras.append([])
        for i in range(0, len(p)):
            letras[cont1].append("_")
        cont1 += 1
fp.close()




print('=' * 50)
print(f'{"RODA A RODA":^50}')
print('=' * 50)


print('\nPrimeiro digite os nomes dos 3 participantes:')

# Sorteando o jogador 
for i in range(0,3,1):
    j = input(f"- Nome do jogador {i+1}: ")
    jogadores.append(j)

print('\nDICA: Jogos')

sleep(0.5)

rodada = 1

while acertou == 0:  # 0 -> não | 1 -> sim 
    roleta_rodada = 1

    print()
    print('=-' * 25)
    print(f'{f"COMEÇO DA RODADA {rodada}":^50}')
    print('=-' * 25)
    print()

    sleep(1)


    while jogadas_rodada == 0:
        if cont == 3:
            cont = 0
        # ------------ Girando a roleta ------------

        # menu
        print('~' * 50)
        print(f'{f"JOGADOR: {jogadores[cont]}":^50}')
        print(f'{f"SALDO: {saldos[cont]}":^50}')
        print('~' * 50)

        sleep(1)

        # LOOP GIRO DA ROLETA

        while roleta_rodada == 1:
            index = [[], [], []]
            print()
            print('-' * 50)
            print(f'{"GIRO DA ROLETA":^50}')
            print('-' * 50)
            print()

            enter = input('Pressione ENTER para girar a roleta!') # rodar roleta
            sleep(1)

            # abrir csv
            with open('d:/palavras.csv', 'r', encoding='UTF-8') as fp:
                palavras = csv.reader(fp)

                # resultao da roleta
                roleta_giro = random.choice(roleta)
                print(f'\nVocê tirou {roleta_giro}', end='')
                print('na roleta!')
                sleep(1)
                
                if roleta_giro=='pv\n': # passa vez
                    novo_saldo == saldos[cont]
                    roleta_rodada = 0

                    cont += 1 # define o jogador    
                    
                elif roleta_giro == 'pt\n': # perde tudo
                    saldos[cont] = 0
                    roleta_rodada = 0
                    cont += 1 # define o jogador    
                    
                else: # qualquer valor inteiro
                    
                    roleta_giro = int(roleta_giro)
                    
                    # escolha da letra
                    while letra_verificacao == 0:
                        acertos = 0
                        letra = input('\nEscolha uma letra de A a Z: ').lower()
                        if letra in letras_excluidas:
                            print("\nLetra já usada! Digite novamente")
                        else:
                            letra_verificacao = 1
                        letras_excluidas.append(letra)
                    letra_verificacao = 0
                        
                    #for p in palavras:
                        #acertos = re.findall(fr'{letra}', p)

                    for ps in palavras:
                        for p in ps:
                            for l in range(0, len(p)):
                                if letra == p[l]:
                                    acertos += 1
                                    index[cont3].append(l) # adiciona o index da letra acertada

                                    for i in range(0,(len(index[cont3]))):
                                        letras[cont3][index[cont3][i]] = letra
                            
                            for i in range(0,(len(index[cont3]))):
                                
for item in minha_lista:
    if '_' in item:
        ocorrencias.append(item)
                                if tracos<=3:
                                    print('Você deseja chutar as palavras?(s/n) ').lower().strip()
                                    resp= input()
                                    if resp == 's':
                                        palavra1 = input('Palavra 1:')
                                        palavra2 = input('Palavra 2:')
                                        palavra3 = input('Palavra 3:')
                                        if palavra1=='entretenimento' and palavra2=='multiplayer' and palavra3=='conquista':
                                            print('Parabens, Você ganhou o jogo!')
                                            continue
                                        else:
                                            print('Você perdeu tudo!')
                                            saldos[cont3] = 0
                                        
                            cont3 += 1

                        if acertos > 0:
                            print(f'\nVocê acertou {acertos} com a letra "{letra}"!')
                        else:
                            print('Você ERROU!')
                    cont3 = 0

                    if acertos == 0:
                        cont += 1 # define o jogador    
                        roleta_rodada = 0
                        print()
                        
                    else:
                        novo_saldo = roleta_giro * acertos
                        saldos[cont] += novo_saldo
    
        if cont ==3:
            jogadas_rodada = 1
        roleta_rodada = 1

    sleep(1)
    print('=-' * 25)
    print(f'{f"FIM DA RODADA {rodada}":^50}')
    print('=-' * 25)
    sleep(1)


    print('-' * 30)
    print(f'{f"Letras erradas: "}')
    for l in letras_excluidas:
        print(f'- {l}', end="")
    print(f'Palavra 1: {letras[0]}')
    print(f'Palavra 2: {letras[1]}')
    print(f'Palavra 3: {letras[2]}')
    print('-' * 30)

    for i in range(0, len(jogadores)):
        print('-' * 30)
        print(f'- Jogador: {jogadores[i]}')
        print(f'- Saldo: {saldos[i]}')
        print('-' * 30)
        sleep(1)
        
    rodada += 1
    jogadas_rodada = 0