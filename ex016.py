# Exercício 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc
numero = float(input('Digite um número para definir sua parte inteira: '))
print(f'A parte inteira do número {numero} é ', trunc(numero))
