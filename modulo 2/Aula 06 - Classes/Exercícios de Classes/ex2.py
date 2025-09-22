class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")


# Criando as pessoas
p1 = Pessoa("João", 25)
p2 = Pessoa("Maria", 30)

# Chamando o método apresentar
p1.apresentar()
p2.apresentar()
