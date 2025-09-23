contador = 1
soma = 0

while contador <= 5:
    try:
        numero = float(input(f"Digite o {contador}º número: "))
        soma += numero
        contador += 1
    except ValueError:
        print("Entrada inválida! Digite apenas números.\n")

print(f"A soma dos números é: {soma}")