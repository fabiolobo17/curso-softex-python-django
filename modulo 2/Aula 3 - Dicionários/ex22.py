jogadores = {"fabio": 40, "pedro": 25, "felipe": 15}

while True:
    


    
    
    try:

        jogador = input("Escolha o jogador(ou digite 'Sair'): ").lower()
        ponto = int(input("Qual a pontuação quer adicionar: "))
        if jogador == "sair":
            break
    
    except ValueError:
        print("Entrada inválida. Digite um número positivo.")
        continue
        for nome, pontos in jogadores:
    if jogadores[nome] != jogador:
        jogadores[mome] = ponto

    else:
            jogadores[nome][pontos] += ponto

print("f\ Jogadores: {jogadores}")
        