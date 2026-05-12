num = 0
pares = 0
impar = 0
zero = 0

for contador in range(10):
    num = int(input('Digite um numero inteiro: '))
    if num % 2 == 0 and num != 0:
        pares +=1
    elif num % 2 != 0 and num != 0:
        impar += 1
    if num == 0:
        zero +=1

print('pares: ',pares)
print ('impares: ',impar)
print('Zeros: ', zero)
        