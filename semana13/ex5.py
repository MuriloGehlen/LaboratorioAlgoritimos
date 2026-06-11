

def maiormenor(valores,producao):
    maior = 0
    menor = 0
    for i in range (5):
        valores = int(input('Digite o valor da produção'))
        for i in producao:
            if valores > i:
                i +=1
            else:
                break
        producao.insert(valores)
    print(producao)
        




def main():
    maior = 0
    menor = 999**999
    valores = 0
    producao = []
    maiormenor(valores, producao)

    
main()