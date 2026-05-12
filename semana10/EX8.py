num = 0
dentro = 0
fora = 0

for contador in range(5):
    num = int(input('Digite um numero:'))
    if num in range(10,21):
        dentro +=1
    else:
        fora +=1

print(dentro,'Numeros estão dentro do intervalo')
print(fora,'numeros estão fora do intervalo')
        
        