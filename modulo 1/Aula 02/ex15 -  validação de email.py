while True:
    
    email = input("Digite seu email: ")
    if "@" in email:
        print("email valido")
        break
    else:
        print("❌ E-mail inválido. Digite novamente.\n")
        