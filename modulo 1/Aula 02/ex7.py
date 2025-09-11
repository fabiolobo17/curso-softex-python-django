idade = int(input("Digite a idade: "))
if 0 < idade <= 12:
    print("é uma criança")
elif 13 < idade <= 17:
    print("é um adolescente")
elif 18 < idade <= 59:
    print("é um adulto")
else:
    print("é um idoso")
