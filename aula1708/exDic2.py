pokemons = {

    "pokemon1" :{"nome" : "BULBASAUR", "tipo" : "GRASS"},
    "pokemon2" :{"nome" : "IVYSAUR", "tipo" : "GRASS"},
    "pokemon3" :{"nome" : "VENUSAUR", "tipo" : "GRASS"},

    "pokemon4" :{"nome" : "CHARMANDER", "tipo" : "FIRE"},
    "pokemon5" :{"nome" : "CHARMELEON", "tipo" : "FIRE"},
    "pokemon6" :{"nome" : "CHARIZARD", "tipo" : "FIRE"},

    "pokemon7" :{"nome" : "SQUIRTLE", "tipo" : "WATER"},
    "pokemon8" :{"nome" : "WARTOTLE", "tipo" : "WATER"},
    "pokemon9" :{"nome" : "BLASTOISE", "tipo" : "WATER"},

    "pokemon10" :{"nome" : "PIKACHU", "tipo" : "ELETRIC"}
}

print("Escolha um tipo de pokémon dentre Grass, Fire, Water ou Eletric")
escolha = input()
contador = 0
for i in pokemons.values():
    if i["tipo"] == escolha.upper():
        contador +=1      
print(f"Existem {contador} Pokémons do tipo {escolha} na lista:")
for i in pokemons.values():
    if i["tipo"] == escolha.upper():
        print(i["nome"])
        

