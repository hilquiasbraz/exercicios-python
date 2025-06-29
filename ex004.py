# Exercício 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

print('=' * 50)
print('\033[36;43mDigite algo para saber seu tipo primitivo:\033[m ')
print('=' * 50)
caractere = input()
print('O tipo primitivo desse valor é :', type(caractere))
print('É alfanumérico? ', caractere.isalnum())
print('É um título? ', caractere.istitle())
print('Todas as letras são maiúsculas? ', caractere.isupper())
print('Todas as letras são minúsculas? ', caractere.islower())
print('Só tem letras? ', caractere.isalpha(), end=', ')
print('Só tem números? ', caractere.isnumeric())
