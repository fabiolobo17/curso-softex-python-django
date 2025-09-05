acessos = [("Pedro", "sucesso"), ("Ana", "Falha"), ("Maria", "Sucesso"), ("Pedro", "Falha"), ("Ana", "Falha")]

conjunto1 = set()
conjunto2 = set()
for nome, status in acessos:
    if status == "sucesso":
        conjunto1.add(nome)
    elif status == "falha":
        conjunto2.add(nome)
        
somente_falha = conjunto2.difference(conjunto1)
print(conjunto1)
print(somente_falha)
