vendas_filtradas = []
produtos = set()
contador = 0
vendas = [("Teclado", 50, 2), ("Mouse",25.50, 4), ("Monitor", 300, 1), ("Fone", 45, 1), ("Webcam", 75.20, 2)]
for nome,preco,qtde in vendas:
    total = qtde * preco
    if total >= 100:
        vendas_filtradas.append((nome, preco, qtde))
    
    produtos.add(nome)
print(vendas_filtradas)
print(produtos) 

        
        
    