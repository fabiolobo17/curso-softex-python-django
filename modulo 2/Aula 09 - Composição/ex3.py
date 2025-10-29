class Ponto:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

class SegmentoDeReta:
    def __init__(self, ponto1:Ponto, ponto2:Ponto):
        self.ponto1 = ponto1
        self.ponto2 = ponto2
    def comprimento(self):
        coord1 = (self.ponto1.x, self.ponto1.y)
        coord2 = (self.ponto2.x, self.ponto2.y)
        resultado = math.dist(coord1, coord2)
        print(resultado)

ponto1 = Ponto(0, 2)
ponto2 = Ponto(3, 5)
segmento = SegmentoDeReta(ponto1, ponto2)
segmento.comprimento()
