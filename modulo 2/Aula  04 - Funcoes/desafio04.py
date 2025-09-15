def mostrar_menu() -> None:
    print("\n=== AGENDA DE CONTATOS ===")
    print("1 - Adicionar contato")
    print("2 - Remover contato")
    print("3 - Procurar contato")
    print("4 - Listar todos")
    print("5 - Sair")


def adicionar_contato(agenda: dict[str, dict[str, str]]) -> None:
    nome = input("Digite o nome: ").strip()
    if nome in agenda:
        print(f"Erro: O contato '{nome}' já existe!")
        return

    telefone = input("Digite o telefone: ").strip()
    email = input("Digite o e-mail: ").strip()

    agenda[nome] = {"telefone": telefone, "email": email}
    print(f"Contato '{nome}' adicionado com sucesso!")


def remover_contato(agenda: dict[str, dict[str, str]]) -> None:
    nome = input("Digite o nome do contato que deseja remover: ").strip()
    if nome in agenda:
        del agenda[nome]
        print(f"Contato '{nome}' removido com sucesso!")
    else:
        print(f"Erro: Contato '{nome}' não encontrado!")


def procurar_contato(agenda: dict[str, dict[str, str]]) -> None:
    nome = input("Digite o nome do contato: ").strip()
    if nome in agenda:
        contato = agenda[nome]
        print(f"Nome: {nome} | Telefone: {contato['telefone']} | E-mail: {contato['email']}")
    else:
        print(f"Contato '{nome}' não encontrado!")


def listar_contatos(agenda: dict[str, dict[str, str]]) -> None:
    if not agenda:
        print("Nenhum contato salvo.")
        return

    print("\n--- Contatos Salvos ---")
    for i, (nome, dados) in enumerate(agenda.items(), start=1):
        print(f"{i}. {nome} - {dados['telefone']} - {dados['email']}")


def main() -> None:
    agenda: dict[str, dict[str, str]] = {}

    while True:
        mostrar_menu()
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Erro: Digite apenas números de 1 a 5.")
            continue

        if opcao == 1:
            adicionar_contato(agenda)
        elif opcao == 2:
            remover_contato(agenda)
        elif opcao == 3:
            procurar_contato(agenda)
        elif opcao == 4:
            listar_contatos(agenda)
        elif opcao == 5:
            print("Encerrando a agenda... Até logo!")
            break
        else:
            print("Opção inválida! Escolha entre 1 e 5.")


if __name__ == "__main__":
    main()
