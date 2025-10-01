from estudante import Estudante  # Importa a classe Estudante

class Escola:
    def __init__(self):
        self.estudantes = []  # Lista para armazenar objetos Estudante

    def adicionar_estudante(self, estudante):
        """Adiciona um estudante na lista."""
        if isinstance(estudante, Estudante):
            self.estudantes.append(estudante)
        else:
            print("Erro: apenas objetos do tipo Estudante podem ser adicionados.")

    def mostrar_relatorio(self):
        """Exibe um relatório de todos os estudantes na escola."""
        print("===== RELATÓRIO DE ESTUDANTES =====")
        for estudante in self.estudantes:
            print(f"Nome: {estudante.nome}")
            print(f"Idade: {estudante.idade}")
            print(f"Matrícula: {estudante.matricula}")
            print("Notas:")
            for materia, lista_notas in estudante.notas.items():
                notas_formatadas = ', '.join(str(nota) for nota in lista_notas)
                print(f"  {materia}: {notas_formatadas}")
            print("-----------------------------------")
