class Livro:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor


class Biblioteca:
    def __init__(self):
        # Começa com uma lista vazia de livros
        self.acervo = []

    def adicionar_livro(self, livro: Livro):
        """Adiciona um livro ao acervo"""
        self.acervo.append(livro)

    def listar_livros(self):
        """Lista todos os livros do acervo"""
        if not self.acervo:
            print("A biblioteca está vazia.")
        else:
            print("📖 Acervo da Biblioteca:")
            for livro in self.acervo:
                print(f"- {livro.titulo}, de {livro.autor}")


# Criando biblioteca
biblioteca = Biblioteca()

# Criando alguns livros
livro1 = Livro("Dom Casmurro", "Machado de Assis")
livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien")
livro3 = Livro("1984", "George Orwell")

# Adicionando os livros à biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

# Listando os livros
biblioteca.listar_livros()
