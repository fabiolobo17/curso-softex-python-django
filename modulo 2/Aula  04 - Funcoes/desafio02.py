def mostrar_menu() -> None:
    print("\n=== CALCULADORA ===")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")


def ler_numero(mensagem: str) -> float:
    """Lê um número do usuário, tratando erros."""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: Digite um número válido!")


def calcular(operacao: int, n1: float, n2: float) -> float | None:
    """Executa a operação matemática escolhida."""
    if operacao == 1:
        return n1 + n2
    elif operacao == 2:
        return n1 - n2
    elif operacao == 3:
        return n1 * n2
    elif operacao == 4:
        if n2 == 0:
            print("Erro: Não é possível dividir por zero!")
            return None
        return n1 / n2
    else:
        print("Operação inválida!")
        return None


def main() -> None:
    while True:
        mostrar_menu()
        try:
            opcao = int(input("Escolha a operação: "))
        except ValueError:
            print("Erro: Digite apenas números de 1 a 5.")
            continue

        if opcao == 5:
            print("Encerrando a calculadora... Até mais!")
            break

        n1 = ler_numero("Digite o primeiro número: ")
        n2 = ler_numero("Digite o segundo número: ")

        resultado = calcular(opcao, n1, n2)
        if resultado is not None:
            print(f"Resultado: {resultado}")


# Executa o programa
if __name__ == "__main__":
    main()
