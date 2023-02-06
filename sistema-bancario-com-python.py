menu = '''
#=#=#=#=# Bem Vindo ao Sistema Bancário #=#=#=#=#

[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Sair

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
'''

limite = 500
saldo = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while  True:
    opcao = input(menu)

    if opcao == '1':
        
        valor = float(input('Informe o valor do depósito: '))
        
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
            print(f'#=' * 25)
            print('\nDeposito realizado com sucesso!\n')
            print(f'#=' * 25)
        else: 
            print('\nFalha na operação. O valor informado é inválido\n')

    elif opcao == '2':

        valor = float(input('Informe o valor do saque: '))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saques >= LIMITE_SAQUE
        
        if excedeu_saldo:
            print(f'#=' * 25)
            print('\nFalha na operação. Saldo insufuciente!\n')
            print(f'#=' * 25)

        elif excedeu_limite:
            print(f'#=' * 25)
            print('\nFalha na operação. O valor do saque excede o limite diário!\n')
            print(f'#=' * 25)

        elif excedeu_saque:
            print(f'#=' * 25)
            print('\nFalha na operação. Limite diário de saques excedido!\n')
            print(f'#=' * 25)

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques -= 1
            print(f'#=' * 25)
            print('\nSaque realizado com sucesso!\n')
            print(f'#=' * 25)

        else: 
            print(f'#=' * 25)
            print('\nFalha na operação. Valor inválido\n')
            print(f'#=' * 25)

    elif opcao == '3':
        print(f'#=' * 25)
        print(f'Extrato'.center(50))
        print(f'#=' * 25)
        print(f'\nNão foram realizadas operações na conta.\n' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}\n')
        print(f'#=' * 25)

    elif opcao == '4':
        print(f'#=' * 25)
        print('\nObrigado Por utilizar nosso sistema\n')
        print(f'#=' * 25)
        break
    
    else:
        print(f'#=' * 25)
        print('\nOperação inválida. Selecione a opção desejada\n')
        print(f'#=' * 25)
