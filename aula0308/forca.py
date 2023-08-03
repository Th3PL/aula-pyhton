import random


def inicioJogo():
    print(f"UUU====U  \n"
        + "||     |  \n"
        + "||        \n"
        + "||        \n"  
        + "||        \n"
        + "||        \n" 
        + "||        \n"
        + "  _ _ _ _ _ _ _ _ _")



palavras = ["ABACAXI", "CACHORRO", "ESMERALDA"]
dicas = ["Uma fruta tropical de casca grossa e polpa doce", "Um animal de estimação fiel e leal", "Uma preciosa pedra verde muito valorizada em joias."]
sorteada = random.choice(palavras)
