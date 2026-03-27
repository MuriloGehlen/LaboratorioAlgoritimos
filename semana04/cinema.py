base = float(input('Digite o valor do ingresso: '))
print('Opções de ingresso:')
print(f'1 - Ingresso normal (valor cheio)')
print(f'2 - Estudante (50% de desconto)')
print(f'3 - Criança até 12 anos (paga 40% do valor)')
print(f'4 - Idoso (paga 60% do valor)')

opcao = int(input('Digite a opção de ingresso: '))
if opcao == 1:
    print('Você pagará', base)
elif opcao == 2:
    final = base * 0.5
    print('Você pagará ',final)
elif opcao == 3:
    final = base * 0.4
    print('Você pagará ',final)
elif opcao == 4:
    final = base * 0.6
    print('Você pagará ',final)
else:
    print('Opção inválida')

