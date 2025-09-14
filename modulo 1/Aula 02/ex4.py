senha = "lobo123"
tentativas = 0

while tentativas < 3:
    user = input("Digite a senha: ")
    if user != senha:
        tentativas += 1
        print("Senha incorreta")
    else:
        print("Senha correta")