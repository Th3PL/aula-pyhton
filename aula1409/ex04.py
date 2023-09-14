continuar = ''
try:
    print("Criando Usuário(s)")
    while continuar != 'N':
        nome = input('Nome: ')
        login = input('login: ')
        senha = input('senha: ')
        f = open('d:/'+ login +'.txt', 'a', encoding='UTF-8')
        f.write(login + '\n' + nome + '\n' +  senha)
        f.close
        continuar = input('Deseja continuar? (S/N)').upper()

except FileNotFoundError:
    print("Caminho e/ou arquivo inexistente")
