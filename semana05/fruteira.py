morangos = (float(input('Quantos kilos de morangos serão comprados? ')))
maca = float(input('Quantos kilos de maçã serão compradas? '))

if morangos + maca <= 5:
    valormorango = 2.5 * morangos
    valormaca = 1.8 * maca
elif morangos + maca > 5:
    valormorango = 2.2 * morangos
    valormaca = 1.5 * maca

if morangos + maca > 8 or valormaca + valormorango > 25:
    valorfinal = (valormorango + valormaca) * 0.9
    print('Você comprou',morangos,'kilos de morango e',maca,'kilos de maçã e pagará',valorfinal,'reais')
else:
    valorfinal = valormaca + valormorango
    print('Você comprou',morangos,'kilos de morango e',maca,'kilos de maçã e pagará',valorfinal,'reais')

