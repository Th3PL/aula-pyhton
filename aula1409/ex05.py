print("Entar:")

login = input('Login: ')
senhaDigitada = input('Senha: ')

try:
    f = open('d:/'+ login +'.txt', 'r', encoding='UTF-8')
    f.close()
except OSError:
    print("Login Inválido, tente novamente: ")
    login = input('Login: ')
    senhaDigitada = input('Senha: ')
f = open('d:/'+ login +'.txt', 'r', encoding='UTF-8')
validar = f.readline()
usu = f.readline()
senha = f.readline()
f.close()
while(senha != senhaDigitada):
    print('Senha Inválida!')
    senhaDigitada = input('Senha: ')

print("Acesso concedido!")

print(f"Usuário: {usu} \nLogin: {validar}")



