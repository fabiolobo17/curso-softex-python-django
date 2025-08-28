ingresso = 20
count = 0
pessoas = int(input("Ingresso para qts pessoas?"))
for pessoa in range(pessoas):
    idade = int(input(f"Digite a idade da pessoa {pessoa+1}:"))
    if idade < 12:
        ingresso == 0
        print("Criança não paga ingresso")
    elif 12 <= idade <= 17:
        ingresso == 10
        print("Adolescente paga meia")
        count += 10
    else:
        ingresso == 20
        print("Adulto paga ingresso cheio")
        count += 20
print(f"O total arrecadado foi de R$ {count},00")