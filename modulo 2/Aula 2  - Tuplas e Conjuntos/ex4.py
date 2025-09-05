notas = [("Ana", 9.5), ("João", 8.0)("Maria", 10)("Pedro", 7.5)("Ana", 10)("Carlos", 6.5)]
nota_máxima = 0

for nome,nota in notas:
    if nota > nota_maxima:
        nota_maxima == nota
print(f"A maior nota é {nota_maxima}")

alunos_maior_nota = []
for nome,nota in notas:
    if nota == nota_maxima:
        alunos_maior_nota.append(nome)
        

