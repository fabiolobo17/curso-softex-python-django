class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self._nome: str = nome
        self._idade: int = idade

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def idade(self) -> int:
        return self._idade
