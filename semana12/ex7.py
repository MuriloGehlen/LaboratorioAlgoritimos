def somaImposto(taxaImposto, custo):
    taxaImposto = (taxaImposto / 100) + 1
    custo *= taxaImposto
    return custo 








def main():
    custo = float(input('Digite o custo: '))
    taxaImposto = float(input('Digite a taxa de imposto: '))
    preco = somaImposto(taxaImposto, custo)
    print(preco)
    
main()