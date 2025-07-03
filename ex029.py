# Exercício 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Qual a velocidade do veículo? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você ultrapassou o limite de velocidade que é de 80 Km/h! Você será multado em R$ {multa:.2f}')
else:
    print('Você passou dentro do limite permitido. Dirija com segurança!')
