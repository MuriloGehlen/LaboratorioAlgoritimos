totaloliva = int(input('Digite o total de olivas a serem plantadas: '))
totalfileira = int(input('Digite o total de fileiras disponíveis: '))

fileira = totaloliva / totalfileira
sobra = totaloliva % totalfileira

print ('Serão plantadas',int(fileira),'Sementes por fileira')
print('Sobrará',sobra,'Sementes')