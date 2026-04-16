opcao = 0
venda = 0
caixa = 0
valor = 0

caixa = float(input('Digite o valor atual do caixa: '))
while opcao != 4:
    print('Opções:')
    print('1 - Realizar Venda')
    print('2 - Retirar Dinheiro')
    print('3 - Dinheiro em Caixa')
    print('4 - Sair')
    opcao = int(input('Digite a opção desejada: '))
    
    if opcao == 1:
        venda = float(input('Digite o valor do produto vendido: '))
        caixa += venda
    elif opcao == 2:
        valor = float(input('Digite o valor a ser retirado:'))
        caixa -= valor
    elif opcao == 3:
        print(caixa)
    
    