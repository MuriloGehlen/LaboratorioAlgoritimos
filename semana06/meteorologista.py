cidades = 0
temperatura = 0
medias = 0

while cidades < 10:
    temperatura = int(input('Quantos graus sua cidade ficou? '))
    if temperatura >= 15 and temperatura <= 25:
        medias += 1
    cidades += 1
print('O numero de cidades entre 15 e 25 graus é: ',medias)