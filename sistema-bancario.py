menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0 
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito no valor de R$ {valor:.2f}\n"
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
            input("Por favor, aperte a tecla Enter para continuar")
        else:
            print("Falha na operação. Por favor informe um valor válido.")
    
    elif opcao == "s":
         valor = float(input("Informe o valor do saque: "))

         excedeu_saldo = valor > saldo
         excedeu_limite = valor > limite
         excedeu_saques = numero_saques >= LIMITE_SAQUES

         if excedeu_saldo:
             print("Falha na operação. Você não possui saldo suficiente.")

         elif excedeu_limite:
             print("Falha na operação. O valor do saque excede o limite.")

         elif excedeu_saques:
             print("Falha na operação. O limite de saques diários foi excedido.")

         elif valor > 0:
             saldo -= valor
             extrato += f"Saque no valor de R$ {valor:.2f}\n"
             print(f"Saque de R${valor:.2f} realizado com sucesso!")
             input("Por favor, aperte a tecla Enter para continuar")
             numero_saques += 1
        
         else:
             print("Falha na operação. Por favor informe um valor válido.")
    
    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===============================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")