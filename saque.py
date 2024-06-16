import os

def sacar():
    saldo = float(os.getenv('SALDO'))
    extrato = os.getenv('EXTRATO')
    limite = float(os.getenv('LIMITE'))
    numero_saques = int(os.getenv('NUMERO_SAQUES'))
    limite_saques = int(os.getenv('LIMITE_SAQUES'))

    valor = float(input("Digite o valor do saque: "))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Você não tem saldo suficiente. Por favor, tente novamente mais tarde.")
    elif excedeu_limite:
        print("O valor do saldo excede o limite. Por favor, tente novamente mais tarde.")
    elif excedeu_saques:
        print("Número de saques diários foi excedido. Por favor, tente novamente mais tarde.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R${valor:.2f}\n"
        numero_saques += 1
    else:
        print("Valor informado inválido. Por favor, tente novamente mais tarde.")
    
    os.environ['SALDO'] = str(saldo)
    os.environ['EXTRATO'] = str(extrato)
    os.environ['NUMERO_SAQUES'] = str(numero_saques)
