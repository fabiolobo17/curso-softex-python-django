while True:
    lista1 = input("Digite uma lista para verificar se é um palíndromo: ")
    lista2 = lista1[::-1]
    if lista2 == lista1:
        print("A lista é um palíndromo.")
        break
    else:
        print("A lista não é um palíndromo:")

