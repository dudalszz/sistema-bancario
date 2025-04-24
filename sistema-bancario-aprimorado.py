import textwrap


def menu():
    menu = """
    ================ MENU ================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [q] Sair
    => """
    return input(textwrap.dedent(menu))



def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    else:
        print("Falha na operação. Valor inválido para depósito.")
    return saldo, extrato


def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor <= 0:
        print("Falha na operação. Valor inválido para saque.")
    elif valor > saldo:
        print("Falha na operação. Você não tem saldo suficiente.")
    elif valor > limite:
        print("Falha na operação. O valor do saque excede o limite.")
    elif numero_saques >= limite_saques:
        print("Falha na operação. Limite de saques diários atingido.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R${valor:.2f} realizado com sucesso!")
    return saldo, extrato, numero_saques



def exibir_extrato(saldo, extrato):
    print("\n========== EXTRATO ==========")
    print("Não houve movimentações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("==============================")



def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Já existe um usuário com esse CPF!")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")



def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None



def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Usuário não encontrado, criação de conta encerrada.")



def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(f"Agência: {conta['agencia']}\nC/C: {conta['numero_conta']}\nTitular: {conta['usuario']['nome']}")
        print("=" * 100)



def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES)

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("Obrigado por utilizar nossos serviços.")
            break

        else:
            print("Opção inválida. Tente novamente.")



main()
