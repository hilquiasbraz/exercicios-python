# Exercício 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

print('\033[42m=\033[m' * 42)
print('\033[32m     Calculadora de reajuste salarial     \033[m')
print('\033[42m=\033[m' * 42)
salario = float(input('Qual o seu salário atual? R$ '))
reajuste = salario * (15 / 100)
print(f'O seu novo salário será de R$ {salario + reajuste:.2f}')
