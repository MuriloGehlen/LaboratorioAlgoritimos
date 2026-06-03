def soma(fazendaA,fazendaB,terceiro):
    for i in range(len(fazendaA)):
        terceiro = [fazendaA[0] + fazendaB[0],fazendaA[1] + fazendaB[1],fazendaA[2] + fazendaB[2]]
    return terceiro


def main():
    fazendaA = [ 5, 10, 15]
    fazendaB = [ 3, 6, 9]
    terceiro = []
    somatorio = soma(fazendaA,fazendaB,terceiro)
    print(somatorio)
main()