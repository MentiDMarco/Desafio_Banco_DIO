#a v1 do projeto irá apenas trabalhar com 1 usuário, dessa forma não sendo necessário saber o número da agencia e a conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato

#O sistema deve permitir realizar 3 saques diários com limite máximo de 500 reais por saque. Caso o usuário não tenha saldo em sua conta, o sistema deve exibir uma mensagem dizendo que o saldo é insuficiente, mostrando que o saque não poderá ser efetuado. Todos os saques deverão ser armazenados em uma variável e exibidos na operação de extrato

#O extrato deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Os valores devem ser mostrados usando o formato R$xxx.xx (Ex: 1500.45 = R$1500.45)

# modulo padrao do python para usar variáveis de ambiente
import os
#importando função depositar
from deposito import depositar
#importando funcao sacar
from saque import sacar
#importando a funcaç extrato
from extrato import pegarExtrato

#estudar variáveis de ambiente
os.environ['SALDO'] = str(0)
os.environ['LIMITE'] = str(500)
os.environ['EXTRATO'] = ""
os.environ['NUMERO_SAQUES'] = str(0)
os.environ['LIMITE_SAQUES'] = str(3)

menu = """
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                 Marbank

        [1] - Depositar
        [2] - Saque
        [3] - Extrato
        [0] - Sair

    Por favor, selecione uma
    função: """

# saldo = 0
# limite = 500
# extrato = ""
# numero_saques = 0
# LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))
    if opcao == 1:
        depositar()
        #valor = float(input("Digite o valor do depósito: "))
        #if valor > 0:
        #    saldo += valor
        #     extrato += f"Depósito: R${valor:.2f}\n"
        # else:
        #     print("Erro, o valor informado está inválido")
    elif opcao == 2:
        sacar()
        # valor = float(input("Digite o valor do saque: "))
        # excedeu_saldo = valor > saldo
        # excedeu_limite = valor > limite
        # excedeu_saques = numero_saques >= LIMITE_SAQUES
        # if excedeu_saldo:
        #     print("Você não tem saldo suficiente. Por favor, tente novamente mais tarde.")
        # elif excedeu_limite:
        #     print("O valor do saldo excede o limite. Por favor, tente novamente mais tarde.")
        # elif excedeu_saques:
        #     print("Número de saques diários foi excedido. Por favor, tente novamente mais tarde.")
        # elif valor > 0:
        #     saldo -= valor
        #     extrato += f"Saque: R${valor:.2f}\n"
        #     numero_saques += 1
        # else:
        #     print("Valor informado inválido. Por favor, tente novamente mais tarde.")
    elif opcao == 3:
        pegarExtrato()
        # print(" Extrato ".center(35, "="))
        # print("Nenhuma operação foi executada." if not extrato else extrato)
        # print(f"\nSaldo: R${saldo:.2f}")
        # print("="*35)
    elif opcao == 0:
        break
    else:
        print("Por favor, escolha uma opção válida.")
