class ContaBancaria:
    def __init__(self, titular: str, saldo_inicial: float):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor: float):
        self.saldo += valor
        print(f"💰 Depósito de R$ {valor:.2f} realizado com sucesso!")

    def mostrar_saldo(self):
        print(f"Saldo atual da conta de {self.titular}: R$ {self.saldo:.2f}")


# Criando a conta
conta1 = ContaBancaria("João", 100.00)

# Mostrando saldo inicial
conta1.mostrar_saldo()

# Pedindo valor ao usuário
valor_deposito = float(input("Digite o valor que deseja depositar: R$ "))

# Realizando o depósito
conta1.depositar(valor_deposito)

# Mostrando saldo atualizado
conta1.mostrar_saldo()