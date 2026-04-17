repetir = True
idade = 0
salario = 0
sexo = 0
estadocivil = 0
opcao = 0

while repetir == True:
    idade = int(input('Digite sua idade: '))
    salario = float(input('Digite seu salário: '))
    sexo = input('Digite seu sexo: ').lower()
    estadocivil = input('Digite seu estado civil: ').lower()
    if idade > 0 or idade < 150:
        if salario > 0:
            if sexo == 'f' or sexo == 'm':
                if estadocivil == 's' or estadocivil == 'c' or estadocivil == 'v' or estadocivil == 'd':
                    repetir = False
    
        