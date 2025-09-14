idade = int(input("Digite sua idade: "))
if idade < 18:
    print("Não pode dirigir.")

else:
    user = input("Tem CNH? Digite 'Sim' ou 'Não': ").lower()
    habilitado = user == "sim"

    if habilitado :
        print("Pode dirigir")
    else:
        print("Precisa tirar CNH")
            