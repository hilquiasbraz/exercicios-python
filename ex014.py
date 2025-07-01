# Exercício 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

print('\033[35m=' * 35)
print('     Conversor de Temperaturas     ')
print('=' * 35)
celsius = float(input('Digite a temperatura em graus Celsius que gostaria de converter para Farenheit: '))
farenheit = (celsius * 1.8) + 32
print(f'A temperatura de \033[32m{celsius:.1f} ºC\033[m \033[35mequivale a \033[32m{farenheit:.1f} ºF')
