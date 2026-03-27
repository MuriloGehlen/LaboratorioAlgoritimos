print('opções de kit:')
print('1 - Kit Básico: Número de peito + medalha - R$100,00')
print ('2 - Kit Plus: Número de peito + medalha + camiseta - R$120,00')
print ('3 - Kit Premium: Número de peito + medalha + camiseta + squeeze + boné - R$150,00')



quantia = float(input('Digite quanto você irá pagar: '))
opcao = int(input('Digite a opção de kit: '))

if opcao == 1:
    if quantia >= 100:
        final = quantia - 100
        print('Você receberá um kit básico, seu troco é de: ', final, 'Reais')
    if quantia < 100:
        print('Valor insuficiente')
elif opcao == 2:
    if quantia >= 120:
        final = quantia - 120
        print('Você receberá um kit plus, seu troco é de: ', final, 'Reais')
    if quantia < 120:
        print('Valor insuficiente')
elif opcao == 3:
    if quantia >= 150:
        final = quantia - 150
        print('Você receberá um kit premium, seu troco é de: ', final, 'Reais')
    if quantia < 150:
        print('Valor insuficiente')