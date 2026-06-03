def menu():
    print('1 - inserir lote')
    print('2 - listar lotes')
    print('3 - retirar um lote')
    print('4 - limpar todos os lotes')
    print('5 - Contar quantos lotes tem o código maior que o valor inserido')
    print('6 - verificar se o código está presente')
    print('7 - encontrar maior e menor código')
    print('8 - sair')
    opcao = int (input('opção: '))
    return opcao

def lotes(codigo):
    novo_lote = 1
    
    while novo_lote % 2 == 1:
        novo_lote = int(input('Digite o código do novo lote: '))
        if novo_lote % 2 == 1:
            print('Digite um código par')
    codigo.append(novo_lote)
    return codigo

def listar(codigo):
    print(codigo)
    
def retirar(codigo):
    remover = int(input('Digite o código do lote que deseja remover: ')) 
    codigo.remove(remover)

def limpar(codigo):
    codigo.clear()        

def comparacao(codigo):
    maior = int(input('A produção precisa ser maior que: '))
    qtd = 0
    for num in codigo:
        if num > maior:
           qtd += 1
    print('Existem ',qtd,'lotes com o código maior que ',maior) 

def verificar(codigo):
    verificacao = int(input('Digite o código que deseja verificar: '))
    existe = verificacao in codigo
    if existe == True:
        print('Código encontrado')
    else:
        print('Código não encontrado')

def maiormenor(codigo):
    maior = codigo[0]
    menor = codigo[0]
    
    for numero in codigo:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    print('maior: ',maior,'menor: ', menor)
    
        
         

def main():
    opcao = 0
    codigo = []
    
    while opcao != 8:
        opcao = menu()
        if opcao == 1:
            lotes(codigo)
        elif opcao == 2:
            listar(codigo)
        elif opcao == 3:
            retirar(codigo)
        elif opcao == 4:
            limpar(codigo)
        elif opcao == 5:
            comparacao(codigo)
        elif opcao == 6:
            verificar(codigo)
        elif opcao == 7:
            maiormenor(codigo)
            
main()