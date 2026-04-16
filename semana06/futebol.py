idade = 0
salario = 0
jogadores = 0
posicao = 'a' or 'd'
maior = 0
menor = 200
salarioataca = 0
atacantes = 0
defensores = 0
salariototal = 0

while jogadores < 10:
    print(jogadores)
    salario = (float(input('Digite o salario do jogador: ')))
    salariototal += salario
    idade = int(input('Digite a idade: '))
    if maior < idade:
        maior = idade
    if menor > idade:
        menor = idade
    posicao = input('Digite sua posição, A ou D: ').lower()
    if posicao == 'a' and salario <= 10000:
        salarioataca += 1
    if posicao == 'a':
        atacantes += 1
    elif posicao == 'd':
        defensores += 1
    jogadores += 1
    
media = salariototal / 10
print('A média dos salários é de ',media)
print('mais novo: ',menor, 'mais velho :',maior)
print('Quantidadade de atacantes com salários até 10.000,00: ',salarioataca)
print('Quantidade de atacantes: ',atacantes,'quantidade de defensores: ',defensores)