import random

def intersecao_listas(lista1, lista2):
    # Usamos set() para eliminar repetições e facilitar a interseção
    intersecao = set(lista1) & set(lista2)
    # Convertemos de volta para lista
    return list(intersecao)

# Gerar duas listas de 10 números inteiros aleatórios entre 1 e 20
lista1 = [random.randint(1, 20) for _ in range(10)]
lista2 = [random.randint(1, 20) for _ in range(10)]

# Exibir as listas
print("Lista 1:", lista1)
print("Lista 2:", lista2)

# Calcular e exibir a interseção
resultado = intersecao_listas(lista1, lista2)
print("Elementos presentes em ambas as listas (sem repetição):", resultado)