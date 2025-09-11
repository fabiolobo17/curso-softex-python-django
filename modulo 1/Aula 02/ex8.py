valor = float(input("Digite sua nota: "))
while 0 > valor or valor > 10.0:
    valor = float(input("Valor incorreto. Digite sua nota: "))
else:
    if valor >= 9.0:
        print("Conceito A")
    elif valor >= 7.0:
        print("Conceito B")
    elif valor >= 5.0:
        print("Conceito C")
    else:
        print("Conceito D")