
def funcodigo(array):
    for i in range(10):
       codigo = 0
       while codigo <= 1000:
            codigo = int(input("Insira o código:"))
            if codigo > 1000:
                array.append(codigo)
            else:
                print("Insira um código maior que 1000")
    print(array)


def main():
    array = []       
    funcodigo(array)        
main()