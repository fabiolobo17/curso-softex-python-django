vitorias = 0
derrotas = 0
empates = 0

jogo1_mandante = int(input("Digite quantos gols a Seleção fez:"))
jogo1_visitante = int(input("Digite quantos gols o adversário fez:"))
if jogo1_mandante > jogo1_visitante:
    vitorias += 1
elif jogo1_mandante < jogo1_visitante:
    derrotas += 1
else:
    empates += 1
print(f"Placar do jogo 1: Seleção {jogo1_mandante} x {jogo1_visitante} Adversário")

jogo2_mandante = int(input("Digite quantos gols a Seleção fez:"))
jogo2_visitante = int(input("Digite quantos gols o adversário fez:"))
if jogo2_mandante > jogo2_visitante:
    vitorias += 1
elif jogo2_mandante < jogo2_visitante:
    derrotas += 1
else:
    empates += 1
print(f"Placar do jogo 2: Seleção {jogo2_mandante} x {jogo2_visitante} Adversário")

jogo3_mandante = int(input("Digite quantos gols a Seleção fez:"))
jogo3_visitante = int(input("Digite quantos gols o adversário fez:"))
if jogo3_mandante > jogo3_visitante:
    vitorias += 1
elif jogo3_mandante < jogo3_visitante:
    derrotas += 1
else:
    empates += 1
print(f"Placar do jogo 3: Seleção {jogo3_mandante} x {jogo3_visitante} Adversário")

jogo4_mandante = int(input("Digite quantos gols a Seleção fez:"))
jogo4_visitante = int(input("Digite quantos gols o adversário fez:"))
if jogo4_mandante > jogo4_visitante:
    vitorias += 1
elif jogo4_mandante < jogo4_visitante:
    derrotas += 1
else:
    empates += 1
print(f"Placar do jogo 4: Seleção {jogo4_mandante} x {jogo4_visitante} Adversário")

jogo5_mandante = int(input("Digite quantos gols a Seleção fez:"))
jogo5_visitante = int(input("Digite quantos gols o adversário fez:"))
if jogo5_mandante > jogo5_visitante:
    vitorias += 1
elif jogo5_mandante < jogo5_visitante:
    derrotas += 1
else:
    empates += 1
print(f"Placar do jogo 5: Seleção {jogo5_mandante} x {jogo5_visitante} Adversário")
print(f"Resultados finais: {vitorias} vitórias, {derrotas} derrotas e {empates} empates.")

