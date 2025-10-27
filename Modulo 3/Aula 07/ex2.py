def rotacionar_lista(lista, k):
    # Garantir que k não seja maior que o tamanho da lista
    k = k % len(lista)
    # Usando slicing para rotacionar para a direita
    return lista[-k:] + lista[:-k]

# Exemplo de uso:
lista = [1, 2, 3, 4, 5]
k = 2

print("Lista original:", lista)
print(f"Lista rotacionada {k} posições para a direita:", rotacionar_lista(lista, k))