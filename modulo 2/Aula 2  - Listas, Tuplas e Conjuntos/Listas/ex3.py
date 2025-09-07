numeros = [int(x) for x in input("Digite uma lista de números separdos por virgula: ").split(",")]
maior = numeros[0]

for i in numeros:
    if i > maior:
        maior = i

segundo_maior = None
for n in numeros:
    if n != maior:
        if segundo_maior is None or n > segundo_maior:
            segundo_maior = n
print(f"O segundo maior é {segundo_maior}")


