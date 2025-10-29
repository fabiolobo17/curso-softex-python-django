class Carro:
    def __init__(self, modelo: str):
        self.modelo = modelo
        self.nivel_combustivel = 0  # começa vazio

    def abastecer(self, litros: float) -> None:
        """Adiciona combustível ao carro."""
        if litros > 0:
            self.nivel_combustivel += litros
            print(f"⛽ Abastecido com {litros}L. Nível atual: {self.nivel_combustivel}L")
        else:
            print("⚠️ Quantidade inválida para abastecer.")

    def dirigir(self, distancia: float) -> None:
        """Tenta dirigir uma distância. 1 litro = 10 km."""
        consumo = distancia / 10  # cálculo do consumo necessário
        if consumo <= self.nivel_combustivel:
            self.nivel_combustivel -= consumo
            print(f"🚗 O carro andou {distancia} km. Combustível restante: {self.nivel_combustivel:.1f}L")
        else:
            print("❌ Combustível insuficiente para essa viagem.")

