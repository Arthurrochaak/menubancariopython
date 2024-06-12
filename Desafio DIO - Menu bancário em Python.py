menu = """
Bem vindo ao terminal de atendimento bancário.\n
[1] Depositar
[2] Sacar
[3] Extrato

[0] Sair

Informe o serviço: """

saldo = 0
limite_saque = 500
numero_saques = 0
limite_saques = 3
extrato = ""

while True:
    escolha = input(menu)

    if escolha == "1":
        valor = float(input("Informe o valor do depósito: \n R$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito efetuado no valor de: R$ {valor:.2f}\n"
        else:
            print("O valor informado é inválido!")

    elif escolha == "2":
        valor = float(input("Informe o valor do saque: \n R$ "))    
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite_saque
        excedeu_saques = numero_saques > limite_saques
        
        if excedeu_saldo:
            print ("Saldo insuficiente!")

        elif excedeu_limite:
            print ("Essa operação excedeu o limite de saque.")

        elif excedeu_saques:
            print("Você atingiu o número máximo de saques diários.")
        elif valor>0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print ("O valor informado é inválido!")

    elif escolha == "3":
         print ("\n EXTRATO: ")
         print ("Não foram realizadas movimentações." if not extrato else extrato)
         print (f"\nSaldo: R$ {saldo:.2f}\n")
    

    elif escolha == "0":
        break

    else :
        print("Comando inválido.")

