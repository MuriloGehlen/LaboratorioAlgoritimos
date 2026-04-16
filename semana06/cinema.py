pessoas = 0
idade = 0
adultos = 0

while pessoas < 5:
    idade = int(input('insira sua idade: '))
    if idade >= 18:
        adultos += 1
    pessoas += 1

print('O numero de individos com mais de 18 anos é de: ',adultos)
