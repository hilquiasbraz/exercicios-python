# Exercício 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = int(input('Digite um número entre 0 e 9999: '))
num = str(numero)
print(f'O número {num} possui: \n{num[3]} unidade(s) \n{num[2]} dezena(s) \n{num[1]} centena(s) \n{num[0]} centena(s) de milhar')
