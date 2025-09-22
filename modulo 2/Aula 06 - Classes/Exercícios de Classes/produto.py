
class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco


# Criando as instâncias
p1 = Produto("Caderno", 15.50)
p2 = Produto("Caneta", 3.00)

# Imprimindo os dados
print(f"Produto: {p1.nome}, Preço: R$ {p1.preco:.2f}")
print(f"Produto: {p2.nome}, Preço: R$ {p2.preco:.2f}")
