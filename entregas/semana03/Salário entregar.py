horas = int(input('Quantas horas você trabalha por mês? '))

salario = horas * 35

if salario < 1000:
    salario = salario + 300
print (salario)