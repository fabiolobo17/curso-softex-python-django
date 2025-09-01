numero = 7
contador = 0
for contador in range(1,6):
    ten = int(input("Digite um número: "))
    if ten == numero:
        print("Você acertou!")
        break
    elif ten > numero:
        print("Você errou! Muito Alto")
    elif ten < numero:
        print("Você errou! Muito baixo")
