class Motor:
    def __init__(self, potencia: int):
        # Atributo da classe Motor
        self.potencia = potencia


class Carro:
    def __init__(self, modelo: str, potencia_motor: int):
        # Atributo da classe Carro
        self.modelo = modelo
        # Criando um objeto Motor dentro do Carro
        self.motor = Motor(potencia_motor)

    def exibir_potencia(self):
        # Mostra a potência do motor do carro
        print(f"O carro {self.modelo} possui {self.motor.potencia} cavalos de potência.")
        

# Testando
carro1 = Carro("Fusca", 50)
carro2 = Carro("Ferrari", 600)

carro1.exibir_potencia()
carro2.exibir_potencia()
