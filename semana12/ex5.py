def lernotas():
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    n3 = float(input('Digite a terceira nota: '))
    n4 = float(input('Digite a quarta nota: '))
    n5 = float(input('Digite a quinta nota: '))
    return n1,n2,n3,n4,n5


def calcularmedia(nota1, nota2, nota3, nota4, nota5):
    media =  (nota1 + nota2 + nota3 + nota4 + nota5 / 2)
    return media

def situacao(media):
    if media>= 7:
        print('Aprovado')
    elif media > 4 and media < 7 :
        print('Exame')
    else:
        print('Reprovado')

def main():
    nota1, nota2, nota3, nota4, nota5 = lernotas()
    media = calcularmedia(nota1,nota2, nota3, nota4, nota5)
    situacao(media)
    
main()