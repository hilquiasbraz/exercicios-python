# Exercício 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

distancia = float(input('Qual a distância da viagem? (Em quilômetros) '))
if distancia <= 200:
    valor = distancia * 0.50
    print(f'Com uma distância de {distancia:.1f} Km, a passagem custará R$ {valor:.2f}')
else:
    valor = distancia * 0.45
    print(f'Com uma distância de {distancia:.1f} Km, a passagem custará R$ {valor:.2f}')
    