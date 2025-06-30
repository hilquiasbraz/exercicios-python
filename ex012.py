# Exercício 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print('\033[46m=\033[m' * 43)
print('\033[46m          Calculadora de desconto          \033[m')
print('\033[46m=\033[m' * 43)
preco = float(input('\033[35mQual o preço do produto que gostaria de adicionar o desconto? R$\033[m '))
produto = preco * (5 / 100)
print(f'O valor do produto de \033[31mR$ {preco:.2f}\033[m, com desconto fica \033[32mR$ {preco - produto:.2f}\033[m. \nTotalizando \033[36mR$ {produto:.2f}\033[m de desconto')
