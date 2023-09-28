#RM 550366
import csv
import os

try:
    print("Buscando filme por Gênero")
    escolha = input('Qual gênero você deseja buscar? ')
    with open('d:/films.csv', 'r') as f:
        escreve_csv=csv.writer(f)
        films = csv.reader(f)
        print(f'Filmes de {escolha} em nosso catálogo:')
        for i in films:
            if i[1] == escolha:
                print(i[0])

except FileNotFoundError:
    print("Caminho e/ou arquivo inexistente")