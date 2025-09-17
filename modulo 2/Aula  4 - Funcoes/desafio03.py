def validar_senha(senha: str) -> bool:
    """Valida se a senha tem no mínimo 8 caracteres, letras e números."""
    if len(senha) < 8:
        return False

    tem_letra = False
    tem_numero = False

    for caractere in senha:
        if caractere.isalpha():
            tem_letra = True
        elif caractere.isdigit():
            tem_numero = True

    return tem_letra and tem_numero


def cadastrar_usuario(usuarios: dict[str, str]) -> None:
    nome = input("Digite o nome de usuário: ").strip()
    senha = input("Digite a senha: ").strip()

    if not validar_senha(senha):
        print("Erro: A senha deve ter no mínimo 8 caracteres e incluir letras e números!")
        return

    if nome in usuarios:
        print("Erro: Usuário já existe!")
        return

    usuarios[nome] = senha
    print(f"Usuário '{nome}' cadastrado com sucesso!")


def login(usuarios: dict[str, str]) -> None:
    nome = input("Digite o nome de usuário: ").strip()
    senha = input("Digite a senha: ").strip()

    if usuarios.get(nome) == senha:
        print(f"Login bem-sucedido! Bem-vindo, {nome}.")
    else:
        print("Erro: Usuário ou senha incorretos!")


def mostrar_menu() -> None:
    print("\n=== SISTEMA DE LOGIN ===")
    print("1 - Cadastrar usuário")
    print("2 - Fazer login")
    print("3 - Sair")


def main() -> None:
    usuarios: dict[str, str] = {}

    while True:
        mostrar_menu()
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Erro: Digite apenas números (1, 2 ou 3).")
            continue

        if opcao == 1:
            cadastrar_usuario(usuarios)
        elif opcao == 2:
            login(usuarios)
        elif opcao == 3:
            print("Encerrando o sistema... Até logo!")
            break
        else:
            print("Opção inválida! Escolha entre 1, 2 ou 3.")


if __name__ == "__main__":
    main()
