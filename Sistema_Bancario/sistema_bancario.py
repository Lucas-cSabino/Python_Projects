import os

saldo = 0
extrato = []
SAQUE_DIARIO = 0
while True:
    command = input(
        "Escolha um comando: \n" +
        "[D] para Depósito \n" +
        "[S] para Saque \n"+
        "[E] para Extrato \n" +
        "[Q] para Sair \n"
        ).upper()
    os.system('clear')

    if command == "D":
        deposito = int(input('Quanto você deseja Depositar? '))
        saldo += deposito
        extrato.append(f'Deposito: R${deposito}')
    elif command == "S":
        if SAQUE_DIARIO > 2:
            print(f'Número máximo de saques diário excedido!: {SAQUE_DIARIO}')
            continue
        else:
            saque = int(input('Quanto você deseja Sacar? '))
            SAQUE_DIARIO += 1
            if saque > saldo:
                print('Saldo insuficiente para saque')
            else:
                saldo -= saque
                extrato.append(f'Saque: R${saque}')
    elif command == "E":
        print('Seu extrato: ')
        for i in extrato:
            print(i)
        print()
        print(f'SEU SALDO É DE: R${saldo}')
    elif command == "Q":
        print('Obrigado, volte sempre! ')
        break
    else:
        print('Por favor, selecione um comando válido.')