a = []
b = []
valor = 0
for i in range(10):
    valor = int(input('Digite um valor: '))
    a.append(valor)
for j in range (i,-1,-1):
    b.append(a[j])
    
print(a)
print(b)
    