num1 = int(input('Digite um numero: '))
num2 = int(input('digite outro numero: '))
if num1 < num2:
    menor = num1
    maior = num2 + 1
elif num1 > num2:
    menor = num2
    maior = num1 + 1

for contador in range(menor,maior):
    if contador % 2 == 0:
        print(contador)