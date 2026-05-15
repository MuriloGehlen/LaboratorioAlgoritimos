elementos = []
valor = 0


for i in range(10):
    valor = int(input('Digite um numero: '))
    elementos.append(valor)
    
for j in range(len(elementos)):
    if elementos[j] % 2 == 0:
        print('posição ',j , ':' ,elementos[j])
        