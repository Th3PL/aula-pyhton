#RM 550366
import json
import os

logs = {}
continuar = ""
try:
    print("Criando Usuário(s)")
    while continuar != 'N':
        nome = input('Nome: ')
        login = input('login: ')
        senha = input('senha: ')
        if os.path.exists('d:/usuarios.json'):
            with open('d:/usuarios.json', 'w') as f:
                logs[login] = {"usuario": nome, "senha": senha}
                json.dump(logs, f)
        continuar = input('Deseja continuar? (S/N)').upper()

except FileNotFoundError:
    print("Caminho e/ou arquivo inexistente")