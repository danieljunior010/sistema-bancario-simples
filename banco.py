saldo = 0.0
extrato = []
saques_diarios = 0

def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("O valor precisa ser positivo.")

def sacar(valor):
    global saldo, saques_diarios
    if saques_diarios >= 3:
        print("Limite de saques diários atingido.")
    elif valor > 500:
        print("Limite de saque por operação é R$ 500.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    else:
        saldo -= valor
        saques_diarios += 1
        extrato.append(f"Saque: R$ {valor:.2f}")
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

def exibir_extrato():
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for operacao in extrato:
            print(operacao)
        print(f"Saldo atual: R$ {saldo:.2f}")

# Exemplo de uso
depositar(1000)
sacar(300)
sacar(600)
sacar(200)
exibir_extrato()
