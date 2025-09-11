preco = float(input("Digite o preço do produto: "))
if preco > 100.00:
    valor_final = preco * 0.90
    print(f"o preço com desconto é R${valor_final:.2f}")