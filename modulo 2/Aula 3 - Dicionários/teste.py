clientes = [{"nome":"Ana", "idade": 21, "cidade": "São Paulo"},
    {"nome": "Bruno", "idade": 30, "cidade": "Rio de Janeiro" },
    {"nome": "Carlos", "idade": 25, "cidade": "São Paulo"},
    {"nome": "Diana", "idade": 45, "cidade": "Belo Horizonte"},
    {"nome": "Eduarda", "idade": 30, "cidade": "Rio de Janeiro"},
    {"nome": "Fábio", "idade": 25, "cidade": "São Paulo"},]

lista1 = {cliente["nome"]: cliente["idade"] for cliente in clientes}
    
print(lista1)

total_clientes = 0
soma_idade = 0

for cliente in clientes:
soma_idade += cliente["idade"]



    