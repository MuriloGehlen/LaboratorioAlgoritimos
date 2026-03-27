pontuacao1 = int(input('Digite a pontuação do time 1: '))
pontuacao2 = int(input('Digite a pontuação do time 2: '))

if pontuacao1 > pontuacao2:
    print ('Time 1 ganhou')
elif pontuacao2 > pontuacao1:
    print ('Time 2 ganhou')
elif pontuacao1 == pontuacao2:
    print('Empate')
    