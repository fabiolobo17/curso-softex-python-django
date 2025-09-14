estoque = [("Camiseta", 101), ("Calça", 102), ("Boné", 103), ("Tênis", 104)]
estoque_online = [("Boné", 103), ("Camisa Polo", 105), ("Calça", 102), ("Chinelo", 106)]

estoque = set(estoque)
estoque_online = set(estoque_online)

produtos = estoque.intersection(estoque_online)
produtos_loja = estoque.difference(estoque_online)
produtos_sites = estoque_online.difference(estoque)

print(produtos)
print(produtos_loja)
print(produtos_sites)