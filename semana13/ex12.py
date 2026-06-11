
def multiplicacao(kg_colhidos , preco_por_kg):
    resultado = []
    for i in range(5):
        multiplicar = preco_por_kg[i] * kg_colhidos[i]
        resultado.append(multiplicar)
    print(resultado)

def main():
    kg_colhidos = [2 , 4 , 6 , 8 , 10]
    preco_por_kg = [3 , 5 , 7 , 9 , 11] 
    multiplicacao(kg_colhidos , preco_por_kg)


main()