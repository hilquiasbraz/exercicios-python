# Exercício 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

from math import trunc
numero = float(input('Digite um número para saber se ele é ÍMPAR ou PAR: '))
numero = trunc(numero)
if numero % 2 == 0:
    print('Este número é PAR')
else:
    print('Esse número é ÍMPAR')
