
def laranjas():
    quantidade = int(input('Digite quantas laranjas vai comprar: '))
    return quantidade

def valor(quantidade):
    if quantidade <= 12:
        preco = quantidade * 0.4
    elif quantidade > 12:
        preco = quantidade * 0.25
    return preco
    

def main():
    quantidade = laranjas()
    preco = valor(quantidade)
    print(preco)
main()