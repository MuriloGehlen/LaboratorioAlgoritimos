
def identificar(array):
    duplicado = 0
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j:
                if array[i] == array[j]:
                    duplicado = 1
    
    if duplicado == 1:
        print("Há duplicatas")
    elif duplicado == 0:
        print("Distintos")


def main():
    array = []
    for i in range(5):
        num = int(input("Insira um número: "))
        array.append(num)
    identificar(array)


main()