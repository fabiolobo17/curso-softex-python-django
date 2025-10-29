class Graodecafe:
    def __init__(self):
        pass
    def moer(self):
        print("Os grãos de café foram moídos")
    
class Agua:
    def __init__(self):
        pass
    def aquecer(self):
        print("A água está aquecida.")

class Cafeteira:
    def __init__(self):
        self.grao = Graodecafe()
        self.agua = Agua()

    def preparar_cafe(self):
        self.grao.moer()
        self.agua.aquecer()
        print("O café está pronto!")

minha_cafeteira = Cafeteira()
minha_cafeteira.preparar_cafe()
