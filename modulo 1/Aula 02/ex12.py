

def ler_numero(posicao: int) -> float:
    """ Pede ao usuario um numero e retorna como float."""
    while True:
        try:
            return float(input(f"Digite o {posicao}º número: "))
        except ValueError:
            print("⚠️ Entrada inválida! Digite apenas números.\n")
                 
def soma_numeros(qtd: int) -> float:
    contador = 1
    soma = 0

    while contador <= qtd:
       numero = ler_numero(contador)
       soma += numero
       contador += 1
    return soma
    
def main() -> None:
    """Função principal do programa."""
    resultado = soma_numeros(5)
    print("A soma dos numeros digitados é:", resultado)

if __name__ == "__main__":
    main()
