elementos = []
valor = 0
soma30 = 0
soma = 0
for i in range(8):
    valor = int(input('Digite um numero: '))
    elementos.append(valor)
    if valor > 30:
        soma30 += valor
    soma += valor

print('valores do vetor: ',elementos)
print('soma > 30', soma30)
print('soma tudo', soma)