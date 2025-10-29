class Funcionario:
    # Atributo de classe (igual para todos os funcionários inicialmente)
    percentual_bonus = 1.10  

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aplicar_bonus(self, percentual):
        """Aplica o bônus informado ao salário do funcionário"""
        fator = 1 + (percentual / 100)  # Converte percentual em fator
        self.salario *= fator


# Criando funcionários
func1 = Funcionario("Ana", 2000)
func2 = Funcionario("Carlos", 3000)

# Lista de funcionários
funcionarios = [func1, func2]

# Mostrando salários iniciais 
print("Salários iniciais:")
for i in range(len(funcionarios)):
    f = funcionarios[i]
    print(f"{i} - {f.nome}: R$ {f.salario:.2f}")

# Pedindo para escolher funcionário
indice = int(input("\nDigite o índice do funcionário para aplicar bônus: "))

# Pedindo novo percentual de bônus
while True:
    try:
        novo_bonus = float(input("Digite o percentual de bônus (0 a 100): "))
        if 0 <= novo_bonus <= 100:
            break
        else:
            print("Digite um valor entre 0 e 100.")
    except ValueError:
        print("Por favor, insira um número válido.")

# Aplicando bônus individualmente
funcionarios[indice].aplicar_bonus(novo_bonus)

# Mostrando salários após o bônus
print("\nSalários após aplicação de bônus:")
for i in range(len(funcionarios)):
    f = funcionarios[i]
    print(f"{f.nome}: R$ {f.salario:.2f}")