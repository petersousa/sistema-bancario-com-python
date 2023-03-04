import textwrap

def menu():
    menu = '''
    #=#=#=#=# Bem Vindo ao Sistema Bancário #=#=#=#=#

    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Nova conta
    [5] - Listar contas
    [6] - Novo usuário
    [7] - Sair

    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
    ''' 
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    
    if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
            print(f'#=' * 25)
            print('\nDeposito realizado com sucesso!\n')
            print(f'#=' * 25)
    else: 
        print('\nFalha na operação. O valor informado é inválido\n')

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saques >= limite_saques
    
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
        numero_saques += 1
        print(f'#=' * 25)
        print(numero_saques)
        print('\nSaque realizado com sucesso!\n')
        print(f'#=' * 25)

    else: 
        print(f'#=' * 25)
        print('\nFalha na operação. Valor inválido\n')
        print(f'#=' * 25)

    return saldo, extrato, numero_saques
   
def exibir_extrato(saldo, /, *, extrato):
    
    print(f'#=' * 25)
    print(f'Extrato'.center(50))
    print(f'#=' * 25)
    print(f'\nNão foram realizadas movimentações na conta.\n' if not extrato else extrato)
    print(f'\nSaldo: R$ {saldo:.2f}\n')
    print(f'#=' * 25)
    
def criar_usuario(usuarios):

    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(f'#=' * 25)
        print("\n=== Já existe usuário com esse CPF! ===")
        print(f'#=' * 25)
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print(f'#=' * 25)
    print("=== Usuário criado com sucesso! ===")
    print(f'#=' * 25)

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:

        print(f'#=' * 25)
        print("\n=== Conta criada com sucesso! ===")
        print(f'#=' * 25)
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print(f'#=' * 25)
    print("\n=== Usuário não encontrado, operação encerrada! ===")
    print(f'#=' * 25)

def listar_contas(contas):
    for conta in contas:
        print(f'#=' * 25)
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print(f'#=' * 25)
        print(textwrap.dedent(linha))


def main():
    
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == '1':
            
            valor = float(input('Informe o valor do depósito: '))
            
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == '2':

            valor = float(input('Informe o valor do saque: '))
            
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == '3':

            exibir_extrato(saldo, extrato=extrato)

       
        elif opcao == '4':

            criar_usuario(usuarios)

        elif opcao == '5': 
            
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == '6':

            listar_contas(contas)
        
        elif opcao == '7': 

            break
        
        else:
            print(f'#=' * 25)
            print('\nOperação inválida. Selecione a opção desejada\n')
            print(f'#=' * 25)

main()