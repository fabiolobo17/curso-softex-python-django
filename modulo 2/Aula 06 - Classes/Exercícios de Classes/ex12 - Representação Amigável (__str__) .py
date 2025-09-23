class Filme:
    def __init__(self, titulo: str, diretor: str, ano: int):
        self.titulo = titulo
        self.diretor = diretor
        self.ano = ano

    def __str__(self):
        """Retorna uma representação amigável do filme"""
        return f"Filme: '{self.titulo}' ({self.ano}) - Diretor: {self.diretor}"


# Criando um objeto Filme
meu_filme = Filme("De Volta para o Futuro", "Robert Zemeckis", 1985)

# Imprimindo o objeto
print(meu_filme)