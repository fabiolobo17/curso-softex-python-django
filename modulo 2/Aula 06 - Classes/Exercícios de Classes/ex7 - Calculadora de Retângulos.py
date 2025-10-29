class Retangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


# Solicitando dados do usuário
base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

# Criando o retângulo com os valores fornecidos
ret = Retangulo(base, altura)

# Calculando e imprimindo resultados
print(f"Área do retângulo: {ret.calcular_area()}")
print(f"Perímetro do retângulo: {ret.calcular_perimetro()}")
