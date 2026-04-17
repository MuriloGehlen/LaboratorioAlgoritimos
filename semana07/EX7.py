estudantes = 0
idade = 0
total = 0

while estudantes < 15:
    idade = int(input('Digite sua idade:'))
    total += idade
    estudantes += 1

media = total / 15

if media <= 25:
    print('Turma jovem')
elif media >= 26 and media <= 60:
    print('Turma adulta')
elif media > 60:
    print('Turma idosa')
    