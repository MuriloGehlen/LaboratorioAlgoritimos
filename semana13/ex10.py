def verificar(array):
    codigo = int(input("Insira um código:"))
    for i in array:
        if codigo == i:
            print ("O código está presente")
            return codigo
        else:
            print("O código não está presente")

def main():
    array = []
    for i in range (5):
        num = int(input("Insira um código:"))
        array.append(num)
    verificar(array)


main()