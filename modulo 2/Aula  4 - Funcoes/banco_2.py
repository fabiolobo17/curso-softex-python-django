"""
programa de banco
1- rodar em loop infinito
2- ter conta e senha(validar)
3- encerrar atendimento
4- cheque especial (limte saldo negativo)
5- tentar 3 vezes a senha
6- opções (saque, deposito, saldo)
7- mostrar saldo apos saque
8- alterar senha
9- dizer nome do usuario
10- pagar boleto
"""

def banco() -> dict:
    """Carrega dados do usuario"""
    return {
        "usuarios":{
            "senha": "9999",
            "nome": "José",
            "saldo": 1500.00,
            "limite_cheque_especial": 500.00,
        },
    },
    "tentativa_login": 3,
    "ultima_conta_base": "123456",
    "digito_verificador": "7",
}


def autenticar_usuario(dados_banco:dict,conta: str, senha: str,) -> tuple[bool, dict | None]:

    """Auntentica o usuario com base na conta e senha. Retorna o status e o usuario"""

    usuario_encontrado = dados_banco["usuarios"].get(conta, Nome) # None == nada
    if usuario_encontrado and usuario_encontrado["senha"] == senha:
        returne True, usuario_encontrado
    returne False, None


def verificar_saldo(usuario:dict) -> None:
    """Mostrar para o usuario o saldo atual dele"""
    print(f"Seu saldo atual é de R${usuario["saldo"]:.2f}")
    print(f"Seu limite de cheque especial é de R${usuario["limite_cheque_especial"]:.2f}")

def cadastrar_cliente(dados_banco:dict) -> None:
    """Cadastra um novo usuario no sistema"""
    print("-----Novo Cadastro de cliente----")

    ultima_conta = dados_banco["ultima_conta_base"]
    nova_conta = int(ultima_conta) + 1

    novo_numero_conta = f"{nova_conta} - {dados_banco["digito_verificador"]}"

    if novo_numero_conta in dados_banco["usuarios"]:
        print("Erro! Esta conta já existe.")
        return

    nova_senha = input("Defina uma senha para sua conta: ")
    nome cliente = input("Defina o nome do cliente: ")

    dados_banco["usuarios"][novo_numero_conta] = {
        "senha": nova_senha,
        "nome": nome_cliente,
        "saldo": 0.00,
        "limite_cheque_especial": 500.00,   
    }
    dados_banco["ultima_conta_base"] = str(nova_conta)
    print(f"Conta criada com sucesso! Cliente {nome_cliente} Seu número de conta é {novo_numero_conta}")

def listar_clientes(banco_dados:dict) -> None:
    """Lista todos os clientes do banco"""
    print("\n-----Lista de Clientes-----")
    if not banco_dados["usuarios"]:
        print("Nenhum cliente cadastrado.")
        return

    for conta, usuario in banco_dados["usuarios"].items():
        print(f"Conta: {conta} - Nome: {usuario['nome']} - Saldo: R${usuario['saldo']:.2f} - Limite Cheque Especial: R${usuario['limite_cheque_especial']:.2f}")
        print("-"*30)

def sacar_valor(usuario:dict) -> None:
    """Realiza o saque de um valor na conta do usuario"""
    try:
        valor_saque = float(input("Informe o valor a ser sacado: R$"))
        if valor_saque <= 0:
            print("Valor inválido! O valor deve ser maior que zero.")
            return

        saldo_disponivel = usuario["saldo"] + usuario["limite_cheque_especial"]
        if valor_saque > saldo_disponivel:
            print("Saldo insuficiente para realizar o saque.")
            return

        usuario["saldo"] -= valor_saque
        print(f"Saque de R${valor_saque:.2f} realizado com sucesso.")
        verificar_saldo(usuario)
    except ValueError:
        print("Valor inválido! Por favor, insira um número.")   





#declaração de constantes
conta_corrente = "123456-7"
senha_usuario = "9999"
saldo_atual = 0
limite_saldo_negativo = 500.00
nome_usuario = "José"

while True:
    for i in range(3):
        conta = input("Entre com a sua conta corrente: ")
        senha = input("Entre com sua senha: ")
        if conta == conta_corrente and senha == senha_usuario:
            print(f"Bem vindo {nome_usuario}")
            acesso_permitido = True
            break
        else:
            print("Usuario ou senha inválido!")
            acesso_permitido = False
    if not acesso_permitido:
        break

    while True:
        opcao = input("Escolha uma opção:\n" \
        "1- Ver saldo.\n" \
        "2- Sacar valor.\n" \
        "3- Depositar.\n" \
        "4- Pagar Boleto.\n" \
        "5- Alterar senha.\n" \
        "6- Sair.\n")
       
       
        if opcao == "1":
            print(f"Seu saldo atual é de {saldo_atual}")
        elif opcao == "2":
            valor_a_sacar = float(input("Entre com o valor a ser sacado: "))
            if valor_a_sacar <= (saldo_atual + limite_saldo_negativo):
                saldo -= valor_a_sacar
                print("Saldo liberado, retire seu valor!")
            else:
                print("Saldo insufciente!")
        elif opcao == "3":
            depositar = float(input("Insira o valor a ser depositado: "))
            if depositar > 0:
                saldo += depositar
            else:
                print("Valor Inválido!")
        elif opcao == "4":
            boleto = float(input("Entre com o valor do boleto: "))
            if boleto < (saldo_atual + limite_saldo_negativo):
                saldo_atual -= boleto
                print("Boleto pago!")
            else:
                print("Saldo insuficiente!")
        elif opcao == "5":
            senha_antiga = input("Digite a senha antiga: ")
            senha_nova1 = input("Digite a senha nova: ")
            senha_nova2 = input("Digite novamente a nova senha: ")
            if senha_antiga == senha_usuario and senha_nova1 == senha_nova2:
                senha_usuario = senha_nova1
                print("Senha atualizada com sucesso!")
            else:
                print("Saldo insuficiente!")
        elif opcao == "6":
            print("Atendimento Finalizado")
break
        else:
            print("Opção Inválida!")

