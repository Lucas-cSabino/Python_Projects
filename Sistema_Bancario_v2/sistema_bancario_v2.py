import os

saldo = 0
extrato = []
SAQUE_DIARIO = 0

usuarios = []
contas_corrente = []
numero_conta_sequencial = 1

def depositar(deposito, extrato, saldo):
    saldo += deposito
    extrato.append(f'Deposito: R${deposito}')
    return saldo

def saque(*, saque, saldo):
    global SAQUE_DIARIO

    SAQUE_DIARIO += 1
    if saque > saldo:
        print('Saldo insuficiente para saque')
    else:
        saldo -= saque
        extrato.append(f'Saque: R${saque}')
    return saldo

def exibir_extrato(extrato, saldo):
    print('Seu extrato: ')
    for i in extrato:
        print(i)
    print()
    print(f'SEU SALDO É DE: R${saldo}')

def sair():
    print('Obrigado, volte sempre!')

def criar_conta():
    nome = input('Digite seu nome: ')
    data_nascimento = input('Digite sua data de nascimento (formato dd/mm/aaaa): ')
    cpf = input('Digite seu CPF (somente números): ')
    endereco = input('Digite seu endereço (formato: lgradouro, nro - bairro - cidade/estado): ')

    for usuario_existente in usuarios:
        if usuario_existente['cpf'] == cpf:
            print('Já existe um usuário com esse CPF. Não é possível cadastrar novamente.')
            return

    novo_usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }
    usuarios.append(novo_usuario)
    print('Conta criada com sucesso!')

def criar_conta_corrente():
    global numero_conta_sequencial
    agencia = "0001"
    numero_conta = numero_conta_sequencial
    numero_conta_sequencial += 1

    print('Selecione o titular da conta: ')
    for i, usuario in enumerate(usuarios, start=1):
        print(f"{i}. {usuario['nome']} - CPF: {usuario['cpf']}")

    try:
        escolha_usuario = int(input('Digite o número correspondente ao titular da conta: '))
        if escolha_usuario < 1 or escolha_usuario > len(usuarios):
            print('Escolha inválida.')
            return

        titular_conta = usuarios[escolha_usuario - 1]
        nova_conta_corrente = {
            'agencia': agencia,
            'numero_conta': numero_conta,
            'titular': titular_conta
        }
        contas_corrente.append(nova_conta_corrente)
        print('Conta corrente criada com sucesso!')

    except ValueError:
        print('Entrada inválida. Digite um número correspondente ao titular da conta.')

def sair():
    print('Obrigado, volte sempre!')

while True:
    command = input(
        "Escolha um comando: \n" +
        "[D] para Depósito \n" +
        "[S] para Saque \n"+
        "[E] para Extrato \n" +
        "[Q] para Sair \n" +
        "[C] para Criar uma conta \n" +
        "[CC] para Criar conta corrente \n"
    ).upper()
    os.system('clear')

    if command == "D":
        valor_deposito = int(input('Quanto você deseja Depositar? \n'))
        saldo = depositar(valor_deposito, extrato, saldo)
        os.system('clear')
        print(f'Valor depositado com sucesso!: {valor_deposito}\n')
    elif command == "S":
        if SAQUE_DIARIO > 2:
            print(f'Número máximo de saques diário excedido!: {SAQUE_DIARIO} \n' )
            continue
        valor_saque = int(input('Quanto você deseja Sacar? '))
        saldo = saque(saque=valor_saque, saldo=saldo)
    elif command == "E":
        exibir_extrato(extrato=extrato, saldo=saldo)
    elif command == "Q":
        sair()
        break
    elif command == "C":
        criar_conta()
    elif command == "CC":
        criar_conta_corrente()
    else:
        print('Por favor, selecione um comando válido. \n')