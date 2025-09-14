entrada = input("Digite uma lista de numeros separados por vírgulas: ")

lista = [int(x) for x in entrada.split(",")]

posicoes = int(input("Digite quantas posições para rotacionar: "))
posicoes = posicoes % len(lista)
lista_rotacionada = []
for i in range(len(lista) - posicoes, len(lista)):
    lista_rotacionada.append(lista[i])
for i in range(lista[0], posicoes):
    lista_rotacionada.append(lista[i])
print(lista_rotacionada)

