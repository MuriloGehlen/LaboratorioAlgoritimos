
def array(lotes):
    inverso = []
    for i in range(10, 0, -1):
        inverso.append(lotes[i-1])
    print(lotes)
    print(inverso)

def main():
    codigos = 0
    lotes = []
    for i in range(10):
        codigos = int(input('Digite os códigos: '))
        lotes.append(codigos)
    array(lotes)
    
main()