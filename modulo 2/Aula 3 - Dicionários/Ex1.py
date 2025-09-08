clientes = [ 
{"nome": "Ana", "idade": 25, "cidade": "São Paulo"}, 
{"nome": "Bruno", "idade": 30, "cidade": "Rio de Janeiro"}, 
{"nome": "Carlos", "idade": 25, "cidade": "São Paulo"}, 
{"nome": "Diana", "idade": 45, "cidade": "Belo Horizonte"}, 
{"nome": "Eduarda", "idade": 30, "cidade": "Rio de Janeiro"}, 
{"nome": "Fábio", "idade": 25, "cidade": "São Paulo"}
]

for cliente in clientes:
    nome = cliente["nome"]
    idade = cliente["idade"]
    print(f"NOme: {nome}, idade: {idade}")

