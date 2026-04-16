contador = 0
codigo = 1

while codigo != 0:
    codigo = int(input('Digite o código do brinquedo ou digite 0 para sair: '))
    if codigo == 1040:
        contador += 1
    print (codigo)
print('O código 1040 foi digitado',contador,'vezes')
