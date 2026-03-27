inscricao = float(input('Digite o valor da inscrição: '))
print ('opções de pagamento:')
print('1 - À vista')
print('2 - Em 2 vezes')
print('3 - Em 3 vezes')
opcao = int(input('Digite a forma de pagamento: '))

if opcao == 1:
    print ('Você pagará',inscricao,'A vista')
elif opcao == 2:
    parcela = inscricao / 2
    print('Você pagará ',inscricao, 'Em 2 parcelas de: ',parcela)
elif opcao == 3:
    parcela = inscricao / 3
    print('Você pagará ',inscricao, 'Em 3 parcelas de: ',parcela)
else:
    print('Opção inválida')
    
    
    