
verificador1 = 0
verificador2 = 0
cpf = []

#validando primeiro digito
def validarPrimeiro(list):

    #nultiplicando algarismos do cpf
    soma = [10, 9, 8, 7, 6, 5, 4, 3 ,2]
    resultado = []
    for i in range(0,9,1):
        valor = list[i] * soma[i]
        resultado.insert(i, valor)
        
    total = sum(resultado)
    resto = total % 11
  
    #validando verificador do primeiro algarismo
    if resto < 2:
        verificador1 = 0
    else:
        verificador1 = 11 -resto

    return verificador1

#validando segundo digito
def validarSegundo(list):
    list.insert(10, validarPrimeiro(list))
    soma = [11, 10, 9, 8, 7, 6, 5, 4, 3 ,2]
    resultado = []
    for i in range(0,10,1):
        valor = list[i] * soma[i]
        resultado.insert(i, valor)

    total = sum(resultado)
    resto = total % 11

  #validando verificador do segundo algarismo
    if resto < 2:
        verificador2 = 0
    else:
        verificador2 = 11 -resto

    return verificador2


#colhendo cpf
print("Digite um cpf: ")
numeros = input()
#convertendo de string para int
numeros = [int(digito) for digito in numeros]
#criando variáveis para verifição dos dois ultimos digitos
doisu = str(numeros[9]) + str(numeros[10])
ultimos = int(doisu)

for digito in numeros:
    cpf.append(digito)


dig1 = cpf[:]
dig1.pop(10)
dig1.pop(9)

comparar = str(validarPrimeiro(dig1)) + str(validarSegundo(dig1))


if(ultimos == int(comparar)):
    print("Cpf valido")
else:
    print("Cpf inválido")




