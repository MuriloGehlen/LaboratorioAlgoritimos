def porcentagem():
    num = int(input("Insira uma porcentagem: "))
    porcento = num / 100
    print("A porcentagem é", porcento)
    return porcento
    

def multiplicacao(azeitonas , extracao):
    arraymultiplicacao =[]
    for item in azeitonas:
        arraymultiplicacao.append(item * extracao)
    return arraymultiplicacao

def main():
    azeitonas = []
    for i in range (6):
        array = int(input("Insira os kilogramas:"))       
        azeitonas.append(array)
    print (azeitonas)
    extracao = porcentagem()
    arraymultiplicacao = multiplicacao(azeitonas , extracao)
    print (arraymultiplicacao)
main()