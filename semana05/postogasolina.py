litros = float(input('Digite quantos litros quer colocar: '))
valor = float(input('Digite o valor: '))

if litros >= 20 and valor > 100:
    preco = valor * 0.90
    print(f'Aplicado 10% de desconto, e o valor final é de: ',valor)
elif litros>= 20 and valor <= 100:
    preco = valor * 0.95
    print(f'Aplicado 5% de desconto, e o valor final é de: ',valor)
else:
    print('Não há desconto')
    