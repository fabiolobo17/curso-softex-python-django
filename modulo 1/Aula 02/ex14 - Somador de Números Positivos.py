soma = 0
while True:
    try:
        num = float(input("Digite um numero para a soma: "))
        if num < 0:
            break
            
        else:
            soma += num


    except ValueError:
        print("Entrada inválida! Digite apenas números.\n")
print("✅ A soma dos números positivos é:", soma)