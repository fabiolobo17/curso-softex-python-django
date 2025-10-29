from pessoa import Pessoa
from typing import Dict, List

class Estudante(Pessoa):
    def __init__(self, nome: str, idade: int, matricula: str) -> None:
        super().__init__(nome, idade)
        self.matricula: str = matricula
        self.notas: Dict[str, List[float]] = {}

    def adicionar_nota_materia(self, materia: str, nota: float) -> None:
        if materia in self.notas:
            self.notas[materia].append(nota)
        else:
            self.notas[materia] = [nota]


# Teste
aluno: Estudante = Estudante("Lucas", 17, "2025A001")
aluno.adicionar_nota_materia("Matemática", 9.0)
aluno.adicionar_nota_materia("Matemática", 8.5)
aluno.adicionar_nota_materia("Português", 7.0)

print("Nome:", aluno.nome)
print("Idade:", aluno.idade)
print("Matrícula:", aluno.matricula)
print("Notas:", aluno.notas)

"""materias:dict[str, list[float]] = {}
def add_nota_materia(materia: str, nota: float):
    aula = materias.get(materia)
    print(f"aula atual: {aula}")

    if aula:
        aula.append(nota)
    else:
        materias[materia] = [nota]
    
    print(f"dicionário de materias: {materias}")

add_nota_materia("matematica", 10.0)
add_nota_materia("matematica", 9.0)"""

 # Setter para adicionar uma nota a uma matéria
    
