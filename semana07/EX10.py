oliveiras = 98
chute = 0

while chute != 98:
    chute = int(input('Digite quantas oliveiras acha que eu possuo: '))
    if chute < 98:
        print('Há mais oliveiras, tente um número maior')
    elif chute > 98:
        print('Há menos oliveiras, tente um número menor')
    elif chute == 98:
        print('Parabéns! Você descobriu a quantidade de oliveiras!')