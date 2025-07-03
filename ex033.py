# Exercício 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))
numero3 = float(input('Digite um terceiro número: '))
if numero1 > numero2 and numero3:
    print('1')
if numero2 > numero1 and numero3:
    print('2')
if numero3 > numero1 and numero3:
    print('3')
