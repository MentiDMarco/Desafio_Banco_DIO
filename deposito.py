import os;

def depositar():
    saldo = float(os.getenv('SALDO'))
    extrato = os.getenv('EXTRATO')

    valor = float(input("Digite o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"
    else:
        print("Erro, o valor informado está inválido")

    os.environ['SALDO'] = str(saldo)
    os.environ['EXTRATO'] = extrato
