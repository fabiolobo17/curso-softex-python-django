lista = list(input("Digite uma lista de itens: "))
remover = input("Digite um item da lista pra remover: ")
if remover in lista:
    lista.remove(remover)
    print(lista)
else:
    print("o item não está na lista")