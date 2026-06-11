




def kg(colheita):
    kilos = 0
    for i in range(5):
        kilos = int(input('Digite o valor da colheita: '))
        colheita.append(kilos)
    return colheita


def inverso(colheita):
    inverso = []
    for i in range(5,0,-1):
        inverso.append(colheita[i-1])
    print(inverso)


def main():
    colheita = []
    kg(colheita)
    inverso(colheita)
main()