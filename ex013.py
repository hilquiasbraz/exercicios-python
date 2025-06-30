# Exercício 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

print('=' * 42)
print('     Calculadora de reajuste salarial     ')
print('\033[42m=\033[m' * 42)
salario = float(input('Qual o seu salário atual? '))
reajuste = salario * (15 / 100)
print(f'O seu novo salário será de R$ {salario + reajuste:.2f}')
