#   Sistema bancário, desafio Python Developer.

print("\nSeja bem-vindo ao sistema bancario PP!\n\nComo podemos lhe atender hoje?")
menu = """
[1] Deposito 
[2] Saque
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
numero_saques = 0

# usando {} é possível definir o nome de cada variável contida em uma lista.
# para armazenar algo espefico na variável desta lista, basta usar o comando "lista["variável da lista"].append(conteúdo a ser armazenado)"

extratos = {
    "Extrato de Deposito": [],
    "Extrato de Saques": [],
    "Extrato Geral": []
}
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

# As condições para depósitos são: 
# Ser um número positivo e inteiro.

    if opcao == "1":
        valor_deposito = (int(input("\nDigite o valor para depósito:\nR$ ")))
        saldo += valor_deposito
        if valor_deposito > 0:
            print(f"\nDepósito realizado com sucesso!\n\nSeu saldo atual é: R${saldo:.2f}\n")
            extratos["Extrato de Deposito"].append(f"R$:{valor_deposito:.2f}")
            extratos["Extrato Geral"].append(f"Deposito R$:{valor_deposito:.2f}")

        else:
            print("Valor para depósito inválido, tente novamente.")

# As condições para saque são:
#  Ser um número positivo e inteiro;
#  Não ser superior a R$500.00; 
#  Máximo de 3 saques diários.

    elif opcao == "2":
        numero_saques += 1
        saques_restantes = (LIMITE_SAQUES - numero_saques)
        
        if numero_saques > LIMITE_SAQUES:
            print("Limite de saques diários atingido.\nTente novamente amanhã ou procure um gerente.\n")
            break
        print("\nDe acordo com o perfil da sua conta você possui 3 saques diários disponíveis.")
        print(f"\nAlém do seu limite por saque ser de R${limite:.2f}.")
        
        valor_saque = (int(input("\nDigite o valor para saque:\nR$ ")))
        
        if valor_saque > saldo:
            print(f"\nNão foi possível realizar a operação!\n\nSaldo em conta insuficiente!\n")
            break
            
        else:
            saldo = saldo - valor_saque

        if valor_saque in range(0, 501):
            print(f"\nSaque realizado com sucesso!\n\nSeu saldo atual é: R${saldo:.2f}\n")
            extratos["Extrato de Saques"].append(f"R$:{valor_saque:.2f}")
            extratos["Extrato Geral"].append(f"Saque R$:{valor_saque:.2f}")

        else:
            print("O limite de saque por saque é R$500.00!\n\nVerifique o valor desejado e refaça a operação.")
            break

# O extrato precisa conter o registro de toda a movimentação realizada.
# Os valores precisam sair no formato "R$xxxx.xx".

    elif opcao == "3":
        while True:
            opcao_de_extrato = int(input("""
    Selecione a opção conforme o tipo de extrato desejado:
                                         
    [1] Extrato Geral
    [2] Extrato de Saques
    [3] Extrato de Depósito
    [4] Sair
                                         
    => """))
            if opcao_de_extrato == 1:
                print("\n==========EXTRATO GREAL==========\n")
                for extrato_geral in extratos["Extrato Geral"]:
                    print(f"\n{extrato_geral}")
                print(f"Seu saldo atual é: R${saldo:.2f}")
                print("\n==========OBRIGADO==========\n")
            
            elif opcao_de_extrato == 2:
                print("\n==========EXTRATO DE SAQUES==========\n")
                print("Saques Realizados:")
                for extrato_saque in extratos["Extrato de Saques"]:
                    print(f"\n{extrato_saque}")
                print("\n==========OBRIGADO==========\n")
            
            elif opcao_de_extrato == 3:
                print("\n==========EXTRATO DE DEPÓSITOS==========\n")
                print("Depositos Realizados:")
                for extrato_deposito in extratos["Extrato de Deposito"]:
                    print(f"\n{extrato_deposito}")
                print("\n==========OBRIGADO==========\n")
                            
            elif opcao_de_extrato == 4:
                print("Obrigado pela preferencia, volte sempre!")
                break
            
    elif opcao == "4":
        print("\nObrigado pela preferencia, volte sempre!\n")
        break

    else:
        print("Operação Inválida, por favor selecione novamente a operação desejada.")