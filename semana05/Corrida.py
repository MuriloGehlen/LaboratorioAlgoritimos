treinador = input('Digite seu nome: ')
salario = float(input('Digite o salário: '))
tempo = int(input('Digite seu tempo de serviço em anos: '))


if tempo >= 5 and salario <= 2000:
    aumento = salario * 1.10
    print(treinador,f'recebeu um aumento de 10% e o novo salário é de: ', aumento )
else:
    aumento = salario * 1.05
    print(treinador,f'recebeu um aumento de 5% e o novo salário é de: ', aumento )
