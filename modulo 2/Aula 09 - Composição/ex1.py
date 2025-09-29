class Motor:
    def __init__(self):
        pass

    def ligar(self):
        print("O motor ligou")

class Carro:
    def __init__(self):
        self.motor = Motor()

    def ligar_carro(self):
        self.motor.ligar()
  
meu_carro = Carro()
meu_carro.ligar_carro()
