class Pessoa:
    def __init__(self, nome: str, idade: int):
        """Inicializa uma pessoa com nome e idade"""
        self.nome = nome
        self.idade = idade


# Testando a classe
p1 = Pessoa("João", 25)
p2 = Pessoa("Maria", 30)

print(f"{p1.nome} tem {p1.idade} anos.")
print(f"{p2.nome} tem {p2.idade} anos.")
