valores = []
maior100 = 0
valor = 0

for i in range (10):
    valor = int(input('Digite um numero: '))
    if valor > 100:
        maior100 += 1
        valores.append(valor)

print('Quantia de valores maior que 100: ', maior100)
print('Valores maior que 100: ', valores)
        
        
    