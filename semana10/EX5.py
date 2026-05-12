maior = 0
novos = 0
loiro = 0
cabcastanho = 0
preto = 0
idade = 0
sexo = 0
olho = 0
cabelo = 0
especifico = 0
azul = 0
verde = 0
castanho = 0
homem = 0
mulher = 0


for contador in range(3):
    sexo = input('Digite seu sexo, M ou F: ').upper()
    olho = input('Cor dos olhos: A (azul) V(verde) C(castanho): ').upper()
    cabelo = input('Cor do cabelo: L (loiro) C(castanhos) P(preto)').upper()
    idade = int(input('Digite sua idade: '))
    if idade > maior:
        maior = idade
    if idade >= 18 and idade <= 35 and olho == 'V' and cabelo == 'P':
        especifico += 1
    if cabelo == 'L':
        loiro +=1
    if cabelo == 'C':
        cabcastanho +=1
    if cabelo == 'P':
        preto +=1
    if olho == 'A':
        azul +=1
    if olho == 'V':
        verde +=1
    if olho == 'C':
        castanho +=1
    if sexo == 'M':
        homem +=1
    if sexo == 'F':
        mulher +=1
        
porcentoF = (mulher * 100) /3
porcentoM = (homem * 100) /3
porcentoLoiro = (loiro * 100) /3
porcentocabcas = (cabcastanho * 100) /3
porcentopreto = (preto * 100) /3
porcentoazul = (azul * 100) /3
porcentoverde = (verde * 100) /3
porcentocastanho = (castanho * 100) /3

print('Maior idade: ',maior)
print('Individuos com idades entre 18 e 35 anos e tem olhos verdes e cabelos pretos',especifico)
print('Porcentagem com olhos azuis: ',porcentoazul)
print('porcentagem com os olhos verdes: ',porcentoverde)
print('porcentagem com os olhos castanhos: ', porcentocastanho)
print('porcentagem de Loiros: ', porcentoLoiro)
print('porcentagem de pessoas com cabelos castanhos: ',porcentocabcas)
print('Porcentagem de pessoas com cabelos pretos: ',porcentopreto)
print('Porcentagem de Homens: ',porcentoM)
print('Porcentagem de mulheres: ',porcentoF)
