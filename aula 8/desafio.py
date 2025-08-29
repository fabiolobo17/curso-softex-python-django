
# Desafio 1 - Triângulo
# Escreva um programa que solicite ao usuário três valores numéricos inteiros positivos
# representando os lados de um triângulo. O programa deve verificar se os valores fornecidos
# podem formar um triângulo válido, de acordo com a seguinte condição: a soma de dois lados
# deve ser maior que o terceiro lado. Se os valores formarem um triângulo válido, o programa
# deve informar que o triângulo é válido; caso contrário, deve informar que os valores não
# podem formar um triângulo.
count = 0
while count < 1:
        lado1 = input("Insira o primeiro lado do triangulo: ")
        if lado1.isdigit():
                l1 = int(lado1)
                print("Primeiro lado =", l1)
                count += 1
                break
        else:
                print("Erro, digite um numero inteiro positivo valido")
count = 0
while count < 1:    
        lado2 = input("Insira o segundo lado do triangulo: ")
        if lado2.isdigit():
                l2 = int(lado2)
                print("Segundo lado =", l2)
                count += 1
                break
        else:
                print("Erro, digite um numero inteiro positivo valido")

count = 0       
while count < 1:
        lado3 = input("Insira o terceiro lado do triangulo: ")
        if lado3.isdigit():
                l3 = int(lado3)
                print("Terceiro lado =", l3)
                count += 1
                break
        else:
                print("Erro, digite um numero inteiro positivo valido")
if(
l1 < l2 + l3 and 
l2 < l1 + l3 and
l3 < l1 + l2 and
l1 > abs(l2 - l3) and
l2 > abs(l1 - l3) and
l3 > abs(l1 - l2)):
        print(f"Os valores {l1}, {l2} e {l3} podem formar um triangulo valido")
        if l1 == l2 == l3:
                print("O triângulo formado é EQUILÁTERO")
        elif l1 == l2 or l1 == l3 or l2 == l3:
                print("O triângulo formado é ISÓSCELES")
        else:
                print("O triângulo formado é ESCALENO")
else:
    print(f"Os valores {l1}, {l2} e {l3} nao podem formar um triangulo")
