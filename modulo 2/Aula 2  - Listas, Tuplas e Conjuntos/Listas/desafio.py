registros_acessos = []
usuarios_sucesso = set()
tempo_total = 0

while True:
    # Pedir o nome do usuário e validar
    while True:
        usuario = input("Digite o nome de usuário (ou 'parar' para sair): ")
        if usuario.lower() == 'parar':
            break
        if not usuario.isalpha():
            print("⚠ O nome deve conter apenas letras. Tente novamente.\n")
            continue
        # Nome válido
        break

    if usuario.lower() == 'parar':
        break

    # Laço para garantir que o status seja válido
    while True:
        try:
            status = int(input("Digite '1' para 'sucesso' e '2' para 'falha': "))
        except ValueError:
            print("⚠ Erro: digite apenas 1 ou 2.\n")
            continue

        if status not in (1, 2):
            print("⚠ Responda com 1 ou 2 apenas.\n")
            continue

        break  # status válido

    # Laço para garantir que a duração seja um número válido
    while True:
        try:
            duracao = int(input("Digite a duração da sessão em minutos: "))
            break
        except ValueError:
            print("⚠ Erro: a duração deve ser um número inteiro. Tente novamente.\n")

    # Definindo status em texto e atualizando dados
    status_texto = "sucesso" if status == 1 else "falha"
    if status == 1:
        usuarios_sucesso.add(usuario)
        tempo_total += duracao

    # Adiciona o registro à lista
    registros_acessos.append((usuario, status_texto, duracao))

# ---- Saída final ----
print("\n📌 Registro de acessos:", registros_acessos)
print("📌 Usuários com acesso bem-sucedido:", usuarios_sucesso)
print("📌 Tempo total de sessões bem-sucedidas:", tempo_total, "minutos")