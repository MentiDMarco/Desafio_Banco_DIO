import os

def pegarExtrato():
    extrato = os.getenv('EXTRATO')
    saldo = float(os.getenv('SALDO'))
    
    print(" Extrato ".center(35, "="))
    print("Nenhuma operação foi executada." if not extrato else extrato)
    print(f"\nSaldo: R${saldo:.2f}")
    print("="*35)