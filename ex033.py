# Exercício 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))
numero3 = float(input('Digite um terceiro número: '))
if numero1 > numero2 and numero1 > numero3:
    maior = numero1
if numero2 > numero1 and numero2 > numero3:
    maior = numero2
if numero3 > numero1 and numero3 > numero2:
    maior = numero3
# Verificando o menor número
if numero1 < numero2 and numero1 < numero3:
    menor = numero1
if numero2 < numero1 and numero2 < numero3:
    menor = numero2
if numero3 < numero1 and numero3 < numero2:
    menor = numero3
print(f'O maior número digitado foi o {maior:.1f}')
print(f'O menor número digitado foi o {menor:.1f}')
