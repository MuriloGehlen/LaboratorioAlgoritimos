
def hora():
    h = -1
    min = -1
    while h < 0 or h > 24:
        h = int(input('Digite as horas: '))
    while min < 0 or min > 59:
        min = int(input('Digite os minutos: '))
    return h, min


def horario(horas):
    if horas > 12:
        horapm = horas - 12
    return horapm


def main():
    horas, minutos = hora()
    horapm = horario(horas)
    print(horapm,':',minutos)
    
    
    
main()