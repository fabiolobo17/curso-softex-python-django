# Lista inicial de strings (poderia ser gerada ou recebida do usuário)
palavras = ["Abacate", "Banana", "Melancia", "Uva", "Pera", "Kiwi", "Manga"]

print("Lista original:", palavras)

i = 0
while i < len(palavras):
    # Verifica se a string contém 'a' ou 'A' usando lower()
    if 'a' in palavras[i].lower():
        palavras.pop(i)  # Remove o elemento atual
        # NÃO incrementa i, pois a lista ficou menor e o próximo item "desce" de posição
    else:
        i += 1  # Só avança se não removeu nada

print("Lista após remover palavras com 'a' ou 'A':", palavras)