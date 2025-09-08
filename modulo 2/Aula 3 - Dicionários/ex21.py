agenda = {}
while True:

    escolha = int(input("""\n 1  - para adicionar contato
    2 - buscar contato
    3 - Sair\n""")) 


    try:
        if escolha == 1:
            contato = input("Digite um nome: ").lower()
            if contato in agenda:
                    print("Contato já existe")
                    continue
            else:
                    telefone = int(input("Digite um telefone: "))
                    agenda[contato] = telefone
        if escolha == 2:
            for contato, telefone in agenda:
                print(telefone)
                
