def valida(n1, x):
    soma = digito = resto = 0
    cont = x
    for i in n1:
        soma += i * cont
        cont -= i 
    resto = soma % 11
    if resto < 2:
        digito = 0
    else:
        digito = 11 - resto
    return digito

#programa principaç
cpf =  cpfval = ""
cpfnum = []
digiuno = digiduo = capfd1 = cpfd2 = 0
print("Digite seu CPF (Somente digitos)")
cpf = input()
for i in range(0, 9, 1):
    cpfnum.append(int(cpf[i:i+1]))
digiuno = valida(cpfnum, 10)
cpfnum.append(digiuno)
digiduo = valida(cpfnum, 11)
cpfnum.append(digiduo)
for i in cpfnum:
    cpfval += str(i)
cpfd1 = int(cpf[9])
cpfd2 = int(cpf[10])
if cpfd1 == digiuno and cpfd2 == digiuno:
    print(f"Seu CPF de número {cpf} é válido")
else:
     print(f"Seu CPF de número {cpf} é inválido")