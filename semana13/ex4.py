


def funsoma(colhidas, soma):
    for i in range(5):
        soma += colhidas[i]
    print('soma total: ',soma)
    return soma
    
def funmedia(adicao):
    media = adicao / 5
    print('a media é: ',media)



def main():
    colhidas = []
    azeitonas = 0
    soma = 0
    for i in range(5):
        azeitonas = int(input('Digite a quantia de azeitonas: '))
        colhidas.append(azeitonas)
    adicao = funsoma(colhidas, soma)
    funmedia(adicao)
main()