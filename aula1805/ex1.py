def situacao(estado) :
    if estado.lower() == "solteiro" :
        print("Você é solteiro")
    else:
        print("Você é casado")
    
print("Digite seu estado civil")
ecivil = input()
situacao(ecivil)
