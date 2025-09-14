acessos = [("Pedro", "sucesso"), ("Ana", "falha"), ("Maria", "sucesso"), ("Pedro", "falha"), ("Ana", "falha")]

conjunto1 = set()
conjunto2 = set()
for nome, status in acessos:
    status = status.lower()  # garante case-insensitive
    if status == "sucesso":
        conjunto1.add(nome)
    elif status == "falha":
        conjunto2.add(nome)
        
somente_falha = conjunto2.difference(conjunto1)
print(conjunto1)
print(somente_falha)
