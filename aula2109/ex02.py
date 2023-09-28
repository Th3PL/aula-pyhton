#RM 550366
import json
import os

try:
    if os.path.exists('d:/usuarios.json'):
        with open('d:/usuarios.json', 'r') as f:
            logs = json.load(f)
    else:
        logs = {}
except FileNotFoundError:
    print("Caminho e/ou arquivo inexistente")

while True:
    login_input = input('Digite seu login (ou digite "S" para sair): ')
    
    if login_input.upper() == 'S':
        break  
    
    senha_input = input('Digite sua senha: ')

    if login_input in logs and logs[login_input]["senha"] == senha_input:
        print(f"Login bem-sucedido para '{login_input}'. Bem-vindo, {logs[login_input]['usuario']}!")
        break  
    else:
        print("Login falhou. Verifique suas credenciais.")
