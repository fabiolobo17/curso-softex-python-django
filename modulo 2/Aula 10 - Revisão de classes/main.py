from escola import Escola
from estudante import Estudante

# 1. Criando uma instância da escola
minha_escola = Escola()

# 2. Criando estudantes
aluno1 = Estudante("Lucas", 17, "2025A001")
aluno2 = Estudante("Ana", 16, "2025A002")

# 3. Adicionando matérias e notas para o aluno1
aluno1.adicionar_nota_materia("Matemática", 9.0)
aluno1.adicionar_nota_materia("Matemática", 8.5)
aluno1.adicionar_nota_materia("Português", 7.0)

# 4. Adicionando matérias e notas para o aluno2
aluno2.adicionar_nota_materia("História", 9.5)
aluno2.adicionar_nota_materia("Matemática", 10.0)

# 5. Adicionando estudantes à escola
minha_escola.adicionar_estudante(aluno1)
minha_escola.adicionar_estudante(aluno2)

# 6. Exibindo o relatório da escola
minha_escola.mostrar_relatorio()
