itens = []
opcao = 0
item = 0
remover = 0

while opcao != 5:
    print('1 - Inserir item')
    print('2 - Retirar item')
    print('3 - Listar itens')
    print('4 - Retirar todos os itens')
    print('5 - Sair')
    opcao = int(input('Digite a opção: '))
    if opcao == 1:
        item = int(input('Digite o numero de um item: '))
        itens.append(item)
    if opcao == 2:
        remover = int(input('Digite o valor a ser removido: '))
        itens.remove(remover)
    if opcao == 3:
        print(itens)
    if opcao == 4:
        itens.clear()