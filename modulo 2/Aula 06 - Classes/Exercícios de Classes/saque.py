class ContaBancaria:
    def __init__(self, titular: str, saldo_inicial: float):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor: float):
        self.saldo += valor
        print(f"💰 Depósito de R$ {valor:.2f} realizado com sucesso!")

    def sacar(self, valor: float):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"🏧 Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("⚠ Saldo insuficiente.")

    def mostrar_saldo(self):
        print(f"Saldo atual da conta de {self.titular}: R$ {self.saldo:.2f}")


# Criando a conta
conta1 = ContaBancaria("João", 100.00)

# Loop interativo
while True:
    print("\n==== MENU ====")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Mostrar Saldo")
    print("4 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Digite o valor que deseja depositar: R$ "))
        conta1.depositar(valor)
    elif opcao == "2":
        valor = float(input("Digite o valor que deseja sacar: R$ "))
        conta1.sacar(valor)
    elif opcao == "3":
        conta1.mostrar_saldo()
    elif opcao == "4":
        print("Saindo do programa. Até mais!")
        break
    else:
        print("⚠ Opção inválida. Tente novamente.")
