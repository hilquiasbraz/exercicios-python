# Exercício 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por Km rodado.

print('\033[45m=\033[m' * 40)
print('     \033[35mCalculadora de aluguel veicular\033[m     ')
print('\033[45m=\033[m' * 40)
quilometros = float(input('Quantos Km o veículo percorreu? '))
tempo = int(input('Por quantos dias ele foi alugado? '))
valor = (quilometros * 0.15) + (tempo * 60)
print(f'O veículo percorreu {quilometros:.1f} Km por {tempo} dia(s) e o valor a ser pago é de R$ {valor:.2f}')
