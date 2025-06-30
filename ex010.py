# Exercício 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

print('\033[41m=\033[m' * 19)
print('\033[41mConversor de Moedas\033[m')
print('\033[41m=\033[m' * 19)
reais = float(input('\033[31mQuantos reais disponíveis você tem para comprar dólares? '))
print(f'Na cotação atual, você comprará \033[32mUS$ {reais / 5.48:.2f}\033[m')
