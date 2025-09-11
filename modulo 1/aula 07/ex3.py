posicao_inicial = 0
posicao_atual = 0

print("Escolha um comando:")
print("\n1 - Avançar")
print("\n2 - Recuar")
print("\n3 - Status")
print("\n4 - Desligar")

while True:
    opcao = int(input("Digite uma opção: "))
    if opcao == 1:
        posicao_atual += 1
        print(f"Posição atual: {posicao_atual}")
    elif opcao == 2:
        posicao_atual -= 1
        print(f"Posição atual: {posicao_atual}")
    elif opcao == 3:
        print(f"Posição inicial: {posicao_inicial}")
        print(f"Posição atual: {posicao_atual}")
    elif opcao == 4:
        print("Desligando...")
        break
    else:
        print("Opção inválida!")
