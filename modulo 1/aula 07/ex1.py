preco = 40.0
cupom = "desc10"
produto = "hamburguer"

while True:
    pedido = input("Digite seu pedido: ").lower()
    if pedido == produto:
        print("Pedido confirmado")
        break
    else:
        print("Este lanche não está cadastrado. Tente novamente.")
entrada_cupom = input("Digite seu cupom: ")
if entrada_cupom == cupom:
    print(f"cupom de 10% válido! o preço do seu hamburguer é:  {preco * 0.90}")
    print("\nPedido a caminho!")
else:
    print(f"Cupom inválido. O preço sem o desconto é de : {preco}")
      