password = "1234"
contador = 1

while contador <= 3:
        num = input(f"Essa é sua {contador}ª tentativa. Digite sua senha: ")
        
        if num == password:
            print("Login bem sucedido!")
            break
        else:
              print("senha incorreta.")
        contador += 1

   
if contador > 3 and num != password:
    print("Tentativas esgotadas")


