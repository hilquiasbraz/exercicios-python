# Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

decimal = int(input('Digite o número inteiro que gostaria de converter: '))
conversao = int(input('Para que base gostaria de converter? \nDigite 0 para BINÁRIO \nDigite 1 para OCTAL \nDigite 2 para HEXADECIMAL \n'))
if conversao == 1:
    binario = 