jornal = 0
jornala = 0
jornalb = 0
jornalc = 0

for contador in range(20):
    jornal = (input('Qual seu jornal favorito? A, B ou C: ')).upper()
    if jornal == 'A':
        jornala +=1
    elif jornal == 'B':
        jornalb +=1
    elif jornal == 'C':
        jornalc +=1

porcento_a = 'A',(jornala * 100) / 20
porcento_b = 'B',(jornalb * 100) / 20
porcento_c = 'C',(jornalc * 100) / 20

porcentagens = [porcento_a,porcento_b,porcento_c]
porcentagens.sort()
print(porcentagens)