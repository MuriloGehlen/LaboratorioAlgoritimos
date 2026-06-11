import random


def pares(array):
    par = []
    impar = []
    numpar = 0
    numimpar = 0
    for i in array:
        if i % 2 == 0:
            numpar += 1
        if i % 2 == 1:
            numimpar += 1
    print ("Existem", numimpar, "números impares")
    print ("Existem", numpar, "números pares")


def main():
    array = []
    for i in range (10):
        num = random.randint(1,50)
        array.append(num)
    pares(array)


main()