nota1 = float(input('Digite uma nota: '))
nota2 = float(input('Digite outra nota: '))
media = (nota1 + nota2) / 2
if media >= 9:
    print('Conceito A, Aprovado!')
elif media < 9 and media >= 7.5:
    print('Conceito B, Aprovado!')
elif media < 7.5 and media >= 6:
    print('Conceito C, Aprovado!')
elif media < 6 and media >= 4:
    print('Conceito D, Reprovado!')
else:
    print('Conceito E, Reprovado!')