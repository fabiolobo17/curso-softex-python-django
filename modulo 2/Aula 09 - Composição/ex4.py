class Teclado:
    def __init__(self):
        pass
    def ligar(self):
        print("O teclado foi ativado.")

class Mouse:
    def __init__(self):
        pass
    def ligar(self):
        print("O mouse foi ativado.")

class Monitor:
    def __init__(self):
        pass
    def ligar(self):
        print("O monitor foi ligado.")


class Computador:
    def __init__(self, teclado, mouse, monitor):
        self.teclado = teclado
        self.monitor = monitor
        self.mouse = mouse

    def ligar(self):
        self.teclado.ligar()
        self.monitor.ligar()
        self.mouse.ligar()

        print("Computador ligado.")

teclado = Teclado()
mouse = Mouse()
monitor = Monitor()

meu_computador = Computador(teclado, mouse, monitor)
meu_computador.ligar()