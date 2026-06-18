from datetime import datetime, timedelta
import matplotlib.pyplot as plt


def menu():
    print('---- MENU------')
    print('1 - Solicitar uma vaga para uma aeronave.')
    print('2 - Retirar uma aeronave do estacionamento.')
    print('3 - Retirar todas as aeronaves do estacionamento.')
    print('4 - Mostrar todas as aeronaves presentes no estacionamento.')
    print('5 - Adiantar o tempo.')
    print('6 - Mostrar informações do tempo do algoritmo.')
    print('7 - Gráfico.')
    print('8 - Sair.')
    opcao = int(input('Digite uma opção: '))
    return opcao


def primeira(estacionamento, filaespera, data, tempo_atual, total_estacionamentos, capacidade):
    aeronave = int(input('Digite o código da aeronave: '))

    if aeronave in estacionamento or aeronave in filaespera:
        print('Essa aeronave já está no estacionamento ou na fila de espera.')

    elif len(estacionamento) < capacidade:
        estacionamento.append(aeronave)
        data.append(tempo_atual)
        total_estacionamentos = total_estacionamentos + 1
        print('Sua aeronave foi deslocada para uma vaga.')

    else:
        if len(filaespera) == 0:
            filaespera.append(aeronave)
            print('Aeronave designada para a fila de espera.')
        else:
            print('Estacionamento e fila de espera cheios. Aeronave enviada para outro aeroporto.')

    return total_estacionamentos


def calcular_valor(data_entrada, data_saida):
    tempo_total = data_saida - data_entrada
    dias = tempo_total.days

    if tempo_total.seconds > 0:
        dias = dias + 1

    if dias < 1:
        dias = 1

    if dias > 30:
        valor = dias * 115
    else:
        valor = dias * 127

    return dias, valor


def segunda(estacionamento, filaespera, data, tempo_atual, total_estacionamentos, total_retiradas, caixa):
    remover = int(input('Digite o código da aeronave a ser removida: '))

    if remover in estacionamento:
        posicao = estacionamento.index(remover)
        data_entrada = data[posicao]
        dias, valor = calcular_valor(data_entrada, tempo_atual)
        estacionamento.pop(posicao)
        data.pop(posicao)
        total_retiradas = total_retiradas + 1
        caixa = caixa + valor

        print('Aeronave removida com sucesso.')
        print('Tempo no estacionamento:', dias, 'dias')
        print('Valor a pagar: ', valor)

        if len(filaespera) > 0:
            aeronave_fila = filaespera[0]

            estacionamento.append(aeronave_fila)
            data.append(tempo_atual)
            filaespera.clear()

            total_estacionamentos = total_estacionamentos + 1

            print('A aeronave da fila de espera foi colocada em uma vaga.')

    else:
        print('Aeronave não encontrada no estacionamento.')

    return total_estacionamentos, total_retiradas, caixa


def terceira(estacionamento, filaespera, data, tempo_atual, total_retiradas, caixa):
    for i in range(len(estacionamento)):
        dias, valor = calcular_valor(data[i], tempo_atual)
        print('Aeronave:', estacionamento[i])
        print('Tempo no estacionamento:', dias, 'dias')
        print('Valor a pagar: ', valor)

        total_retiradas = total_retiradas + 1
        caixa = caixa + valor

    estacionamento.clear()
    filaespera.clear()
    data.clear()

    print('Todas as aeronaves foram retiradas do estacionamento.')

    return total_retiradas, caixa


def quarta(estacionamento, filaespera, data, tempo_atual, capacidade):
    if len(estacionamento) == 0:
        print('Não há aeronaves no estacionamento.')

    else:
        for i in range(len(estacionamento)):
            tempo_permanencia = tempo_atual - data[i]

            dias = tempo_permanencia.days
            horas = tempo_permanencia.seconds // 3600
            minutos = (tempo_permanencia.seconds % 3600) // 60
            print('Aeronave:', estacionamento[i])
            print('Entrada:', data[i].strftime('%d/%m/%Y %H:%M:%S'))
            print('Tempo de permanência:', dias,'dias,',horas,'horas e',minutos,'minuto')

    print('Aeronave na fila de espera:', filaespera)
    vagas_livres = capacidade - len(estacionamento)
    print('Vagas livres:', vagas_livres)


def sexta(tempo_atual):
    print('1 - Adiantar em dias')
    print('2 - Adiantar em meses')
    escolha = int(input('Digite uma opção: '))
    quantidade = int(input('Digite a quantidade: '))

    if escolha == 1:
        tempo_atual = tempo_atual + timedelta(days=quantidade)
        print('Tempo adiantado em', quantidade, 'dias.')

    elif escolha == 2:
        tempo_atual = tempo_atual + timedelta(days=quantidade * 30)
        print('Tempo adiantado em', quantidade, 'mês(es).')

    else:
        print('Opção inválida.')

    return tempo_atual


def setima(estacionamento, filaespera, capacidade):
    ocupadas = len(estacionamento)
    livres = capacidade - len(estacionamento)
    espera = len(filaespera)
    nomes = ['Vagas ocupadas', 'Vagas livres', 'Fila de espera']
    valores = [ocupadas, livres, espera]

    plt.bar(nomes, valores)
    plt.title('Situação do estacionamento de aeronaves')
    plt.ylabel('Quantidade')
    plt.ylim(0, capacidade)
    plt.show()


def oitava(tempo_inicial, tempo_atual):
    diferenca = tempo_atual - tempo_inicial
    print('Tempo inicial do algoritmo:', tempo_inicial.strftime('%d/%m/%Y %H:%M:%S'))
    print('Tempo atual do algoritmo:', tempo_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print('Dias simulados:', diferenca.days)


def main():
    capacidade = 5
    estacionamento = []
    filaespera = []
    data = []
    tempo_inicial = datetime.now()
    tempo_atual = tempo_inicial
    total_estacionamentos = 0
    total_retiradas = 0
    caixa = 0
    opcao = 0

    while opcao != 8:
        opcao = menu()
        if opcao == 1:
            total_estacionamentos = primeira(estacionamento, filaespera, data, tempo_atual, total_estacionamentos, capacidade)
        
        elif opcao == 2:
            total_estacionamentos, total_retiradas, caixa = segunda(estacionamento, filaespera, data, tempo_atual, total_estacionamentos, total_retiradas, caixa)

        elif opcao == 3:
            total_retiradas, caixa = terceira(estacionamento, filaespera, data, tempo_atual, total_retiradas, caixa)

        elif opcao == 4:
            quarta(estacionamento, filaespera, data, tempo_atual, capacidade)

        elif opcao == 5:
            tempo_atual = sexta(tempo_atual)

        elif opcao == 6:
            oitava(tempo_inicial, tempo_atual)

        elif opcao == 7:
            setima(estacionamento, filaespera, capacidade)

        elif opcao == 8:
            print('\nEncerrando o sistema...')
            print('Total de estacionamentos realizados com sucesso:', total_estacionamentos)
            print('Total de retiradas de aeronaves:', total_retiradas)
            print('Valor em caixa: R$', caixa)

        else:
            print('Opção inválida.')


main()