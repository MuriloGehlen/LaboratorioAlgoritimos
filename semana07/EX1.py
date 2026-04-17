
oliveiras = 0
maior = 0
menor = 9999999999999999999999
total = 0
dias = 0
diamenor = 0
diamaior = 0


while dias < 7:
    oliveiras = int(input('Digite a quantia de oliveiras colhidas no dia: '))
    total += oliveiras
    if oliveiras < menor:
        menor = oliveiras
        diamenor = dias + 1
    if maior < oliveiras:
        maior = oliveiras
        diamaior = dias + 1
    dias += 1

print('O total de oliveiras é ',total)
print('O dia com a menor colheita foi o dia ',diamenor)
print('O dia com a maior colheita foi o dia',diamaior)


