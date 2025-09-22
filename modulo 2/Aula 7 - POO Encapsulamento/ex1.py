class Pessoa:
    def __init__(self, _nome, _idade):
        self.nome = _nome       # Usa o setter com validação
        self.idade = _idade     # Usa o setter com validação

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome: str):
        if isinstance(novo_nome, str) and novo_nome:
            self._nome = novo_nome
        else:
            print("Nome inválido. Deve ser uma string não vazia.")

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade: int):
        if isinstance(nova_idade, int) and nova_idade >= 0:
            self._idade = nova_idade  # ✅ Aqui está a correção
        else:
            print("Idade inválida. Deve ser um inteiro positivo")
            self._idade = 0  # Valor padrão para casos inválidos

# Teste
nova_pessoa = Pessoa("ghjjh", 10)
print(nova_pessoa.nome)   # Saída: ghjjh
print(nova_pessoa.idade)  # Saída: 10
