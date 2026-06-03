def producaofun(produarray):
    for i in range(8):
        producao = float(input('Digite o valor da producao em kg: '))
        produarray.append(producao)
    return produarray

def media(array,mediaari):
    for x in range(8):
        mediaari += array[x]
    final = mediaari / 8
    return final


def main():
    mediaari = 0
    produarray = []
    array = producaofun(produarray)
    mediafinal = media(array,mediaari)
    print(array)
    print(mediafinal)
main()