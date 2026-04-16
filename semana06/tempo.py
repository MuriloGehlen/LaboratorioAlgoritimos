tempo = 0
corredores = 0
rapidos = 0
lentos = 0
tempototal = 0

while corredores < 7:
    tempo = float(input('Digite o tempo do corredor'))
    if tempo < 30:
        rapidos += 1
    elif tempo >= 30 and tempo <= 60:
        lentos += 1 
    tempototal += tempo
    corredores += 1
porcentagem = (100 * lentos) / 7 
print('A media dos corredores é:',tempototal / 7)
print(rapidos,'Terminaram em menos de 30 minutos')
print(porcentagem,f'% Corredores terminaram entre 30 e 60 minutos')
