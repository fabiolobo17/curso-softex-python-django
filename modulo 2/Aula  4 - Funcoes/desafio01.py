# Lista de todas as vogais minúsculas (com e sem acento)
VOGAIS = [
    "a", "e", "i", "o", "u",
    "á", "é", "í", "ó", "ú",
    "â", "ê", "î", "ô", "û",
    "ã", "õ",
    "à", "è", "ì", "ò", "ù",
    "ä", "ë", "ï", "ö", "ü"
]


def contar_vogais_consoantes(frase: str) -> tuple[int, int]:
    """Conta vogais (inclusive acentuadas) e consoantes."""
    qtd_vogais = 0
    qtd_consoantes = 0

    frase = frase.lower()  # converte tudo para minúsculo

    for letra in frase:
        if letra.isalpha():
            if letra in VOGAIS:
                qtd_vogais += 1
            else:
                qtd_consoantes += 1
    return qtd_vogais, qtd_consoantes


def eh_palindromo(frase: str) -> bool:
    """Verifica se a frase é palíndromo, ignorando espaços e maiúsculas."""
    somente_letras = ""
    frase = frase.lower()

    for letra in frase:
        if letra.isalpha():
            somente_letras += letra
    return somente_letras == somente_letras[::-1]


def analisar_frase(frase: str) -> None:
    """Mostra resumo da análise da frase."""
    palavras = frase.split()
    qtd_palavras = len(palavras)

    qtd_vogais, qtd_consoantes = contar_vogais_consoantes(frase)
    palindromo = eh_palindromo(frase)

    print("\n--- Resumo da Análise ---")
    print(f"Palavras: {qtd_palavras}")
    print(f"Vogais: {qtd_vogais}")
    print(f"Consoantes: {qtd_consoantes}")
    print(f"É um palíndromo? {'Sim' if palindromo else 'Não'}")


# Programa principal
frase_usuario: str = input("Digite uma frase para analisar: ")
analisar_frase(frase_usuario)
