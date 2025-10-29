class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print("Ola meu nome e", self.nome, " e tenho", self.idade, "anos.")
    
class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso
        
    def apresentar(self):
        print(f"Olá meu nome é {self.nome}, tenho {self.idade} anos e curso {self.curso}.")

pessoa = Pessoa("Fabio", 48)
estudante = Estudante("Ana", 22, "Engenharia")

familia: list[Pessoa] = [pessoa, estudante]
for i in familia:
    i.apresentar()