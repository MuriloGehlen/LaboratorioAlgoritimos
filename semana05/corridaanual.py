print('Responda as perguntas com sim ou não')
p1 = input('Você treinou regularmente nas últimas semanas? ').lower()
p2 = input('Participou de treinos longos (acima de 10 km)? ').lower()
p3 = input('Seguiu uma dieta especial para a corrida? ').lower()
p4 = input('Já competiu em provas oficiais neste ano? ').lower()
p5 = input('Conta com acompanhamento de treinador ou equipe? ').lower()
ponto = 0

if p1 == 'sim':
    ponto += 1  
if p2 == 'sim':
    ponto += 1 
if p3 == 'sim':
    ponto += 1
if p4 == 'sim':
    ponto += 1
if p5 == 'sim':
    ponto += 1

print(ponto)
if ponto == 2:
    print('Você é classificado como participante casual')
elif ponto == 3 or ponto == 4:
    print('Você é classificado como Atleta Competitivo')
elif ponto == 5:
    print('Você é classificado como Atleta de Elite')
elif ponto < 2:
    print('Você é classificado como Não Preparado')