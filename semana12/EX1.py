def media():
    n1 = float(input('Digite sua nota: '))
    n2 = float(input('Digite sua outra nota: '))
    valormedia = (n1 + n2) / 2
    return valormedia

def aprovacao(valormedia):
    if valormedia >= 7:
        print('Aprovado')
    else:
        print('reprovado')


def main():
    valormedia = media()
    aprovacao(valormedia)
    
    
main()