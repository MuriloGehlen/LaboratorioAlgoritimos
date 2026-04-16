opcao = 0
clientes = 0
cafe = 0
capuccino = 0
cha = 0

while clientes  < 10:
    print('Opções disponíveis')
    print('A -  Café Expresso')
    print('B - Capuccino')
    print('C - Chá')
    opcao = input('Digite sua opção: ').upper()
    if opcao == 'A':
        cafe += 1
    elif opcao == 'B':
        capuccino += 1
    elif opcao == 'C':
        cha += 1
    clientes += 1
    
porcentagemcafe = (100 * cafe) / clientes
porcentagemcapuccino = (100 * capuccino) / clientes
porcentagemcha = (100 * cha) / clientes

print('Total de votos para o café: ',cafe)
print('Total de votos para o capuccino: ',capuccino)
print('Total de votos para o chá: ',cha)

print('Porcentagens de votos: ')
print('Café:',porcentagemcafe,'Capuccino: ',porcentagemcapuccino, 'Cha: ',porcentagemcha)