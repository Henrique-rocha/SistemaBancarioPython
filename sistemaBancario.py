
menu = '---\n[d] Depositar\n[s] Sacar\n[e] Extrato\n[q] Sair\n---'
saldo = 0
limite = 500
extrato = '---'
numero_saques = 0
LIMITE_SAQUES = 3
while True:
    opcao = input(menu +'\n => ')

    if opcao == 'd':
        valor = float(input('Informe o valor do Deposito: '))
        if valor > 0:
            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f}\n'
        else:
            print('Operação falhou! O valor informado é invalido.')

    elif opcao == 's':
        valor = float(input('Informe o valor do Saque: '))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque  = numero_saques > LIMITE_SAQUES
        if excedeu_saldo:
            print('Operação falhou! Você não tem saldo suficiente.')
        elif excedeu_limite:
            print('Operação falhou! O valor do Saque excede o Limite.')
        elif excedeu_saque:
            print('Operação falhou! O Número Máximo de Saques Excedito.')
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
        else:
            print('Operação falhou! O valor informado é invalido.')
    elif opcao == 'e':
        print('\n=============== EXTRATO ===============')
        print('não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('======================================')
    elif opcao == 'q':
        break
    else:
        print('Operação invalida, por favor selecione novamente a operação desejada.')
        