def dobro(valor):
    dobrovalor = valor * 2
    return dobrovalor


def triplo(valor):
    triplovalor = valor * 3
    return triplovalor


def main():
    valor = float(input('Digite um valor: '))
    dobrovalor = dobro(valor)
    triplovalor = triplo(valor)
    print(dobrovalor)
    print(triplovalor)
    
main()