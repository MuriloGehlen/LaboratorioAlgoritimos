altura = float(input('Digite sua altura: '))
genero = (input('Digite seu genero com H ou M: ')).upper()

if genero == 'M':
    formulam = (62.1 * altura) - 44.7
    print(formulam)
if genero == 'H':
    formulah = (72.7 * altura) - 58
    print(formulah)

    

