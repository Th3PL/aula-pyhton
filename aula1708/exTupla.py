#Aluno Pedro Lucas de Andrade Nunes RM: 550366
pokemons = ("BULBASAUR", "GRASS", "IVYSAUR", "GRASS", "VENUSAUR", "GRASS", "CHARMANDER", "FIRE",  "CHARMELEON", "FIRE",  "CHARIZARD", "FIRE", "SQUIRTLE", "WATER", "WARTOTLE", "WATER", "BLASTOISE", "WATER", "PIKACHU", "ELETRIC")

print("Digite um tipo de Pokémon(Grass, Water, Fire ou Eletric)")
escolhido = input()


print(f"Quantidade de Pokémons do tipo {escolhido} na tupla: {pokemons.count((escolhido.upper()))}")
print(f"Pokémons do tipo {escolhido} na lista: ")
for i in range(0, len(pokemons)-1, 1):
    if pokemons[i+1] == escolhido.upper():
        print(pokemons[i])



