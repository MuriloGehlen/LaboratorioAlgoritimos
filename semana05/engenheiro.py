forca1 = float(input('Digite a 1ª força: '))
forca2 = float(input('Digite a 2ª força: '))
forca3 = float(input('Digite a 3ª força: '))

if forca1 + forca2 > forca3 and forca1 + forca3 > forca2 and forca2 + forca3 > forca1:
    if forca1 == forca2 == forca3:
        forcas = 'Simétrico'
        print(forcas)
    elif forca1 == forca2 or forca2 == forca3 or forca3 == forca1:
        forcas = 'Parcialmente simétrico'
        print(forcas)
    else:
        forcas = 'Assimétrico'
        print(forcas)
else:
    print('Não há equilibrio nas forças')
        