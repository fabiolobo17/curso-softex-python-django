class Comodo:
    def __init__(self, nome):
        self.nome = nome
class Casa:
    def __init__(self):
        self.comodos = []

    def adicionar_comodo(self, nome):
        novo_comodo = Comodo(nome)
        self.comodos.append(novo_comodo)

    def listar_comodos(self):
        print("Cômodos da casa:")
        for comodo in self.comodos:
            print(f"- {comodo.nome}")

minha_casa = Casa()
minha_casa.adicionar_comodo("Sala")
minha_casa.adicionar_comodo("Cozinha")
minha_casa.adicionar_comodo("Quarto")
minha_casa.adicionar_comodo("Banheiro")

minha_casa.listar_comodos()
