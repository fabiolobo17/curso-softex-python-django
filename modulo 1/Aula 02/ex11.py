def ler_numero() -> int:
    """Pergunta um número ao usuário até ele digitar corretamente."""
    while True:
        try:
            return int(input("Digite um número: "))
        except ValueError:
            print("Erro: digite um número inteiro válido!")


def tabuada(num: int) -> None:
    """Imprime a tabuada de 1 a 10 do número informado."""
    n = 1
    while n <= 10:
        resultado = num * n
        print(f"{num} x {n} = {resultado}")
        n += 1


def main() -> None:
    numero = ler_numero()
    tabuada(numero)


if __name__ == "__main__":
    main()
