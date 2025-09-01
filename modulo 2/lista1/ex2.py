numero = 14
count = 0
while count < 5:
    tentativa = int(input("Advinhe o numero de 1 a 20: "))
    count += 1
    if tentativa == numero:
        print("Você acertou!")
        break
    elif tentativa < numero:
        print("Muito baixo. Tente um número maior.")
    else:
        print("Muito alto. Tente um número menor.")
else:
    print(f"Game over. O número era {numero}.")