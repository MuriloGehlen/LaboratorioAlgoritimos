torcedores = 100
ingressos = 0
opcao = 0

while opcao != 4:
    print ('1 - Diminuir quantidade de ingresso')
    print ('2 - Adicionar ingressos extras')
    print ('3 - Mostrar ingressos disponíveis')
    print ('4 - Encerrar')
    opcao = int(input('Digite a opção:'))
    
    if opcao == 1:
        quantidade1 = int(input('Quantos deseja remover? '))
        ingressos -= quantidade1
    elif opcao == 2:
        quantidade2 = int(input('Quantos ingressos deseja adicionar? '))
        ingressos += quantidade2
        if ingressos > 100:
            print('A capacidade máxima do estádio são 100 torcedores')
    elif opcao == 3:
        print(ingressos)
    elif opcao == 4:
        print('Encerrando')
