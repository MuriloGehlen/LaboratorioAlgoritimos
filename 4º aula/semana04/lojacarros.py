valorcarro = float(input('Digite o valor do carro: '))
print('Digite a forma de pagamento:' )
print(f'1 - Pagamento à vista (4% de desconto)')
print(f'2 - Pagamento em 12x (2% de juros)')
print(f'3 - Pagamento em 24x (7% de juros)')
print(f'4 - Pagamento em 36x (15% de juros)')

pagamento = int(input('Digite a forma de pagamento: '))

if pagamento == 1:
    valorfinal = valorcarro * 0.96
    print('Valor do carro: ' ,valorcarro ,'valor com desconto: ', valorfinal)
elif pagamento == 2:
    valorfinal = valorcarro * 1.02
    parcela = valorfinal / 12
    print('Valor do carro: ' ,valorcarro ,'valor com desconto: ', valorfinal, 'Valor da parcela: ',parcela)
elif pagamento == 3:
    valorfinal = valorcarro * 1.07
    parcela = valorfinal / 24
    print('Valor do carro: ' ,valorcarro ,'valor com desconto: ', valorfinal, 'Valor da parcela: ',parcela)
elif pagamento == 4:
    valorfinal = valorcarro * 1.15
    parcela = valorfinal / 36
    print('Valor do carro: ' ,valorcarro ,'valor com desconto: ', valorfinal, 'Valor da parcela: ',parcela)