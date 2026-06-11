import random

def pares(array):
    par = []
    for i in array:
        if i % 2 == 0:
            par.append(i)
    print (par)



def main():
    array = []
    for i in range (10):
        num = random.randint(1,100)
        array.append(num)
    pares(array)


main()