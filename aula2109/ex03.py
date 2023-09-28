#RM 550366
import csv
import os

films = []
continuar = ""
try:
    print("Cadastrando Filme")
    while continuar != 'N':
        filme = input('Filme: ')
        genero = input('Gênero: ')
        duracao = input('duração')
        censura = input('censura: ')
        diretor = input('Diretor: ')
        films.append([filme,genero,duracao,censura,diretor])
        continuar = input('Deseja Cadastrar outro filme? (S/N)').upper()
    with open('d:/films.csv', 'a', newline='') as f:
        escreve_csv=csv.writer(f)
        for i in films:
            escreve_csv.writerow(i)
except FileNotFoundError:
    print("Caminho e/ou arquivo inexistente")