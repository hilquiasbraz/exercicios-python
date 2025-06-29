# Exercício 005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

print('\033[33m~\033[m' * 62)
print('\033[45mDigite um valor para descobrir seu antecessor e seu sucessor:\033[m ')
print('\033[33m~\033[m' * 62)
valor = int(input())
antecessor = int(valor - 1)
sucessor = int(valor + 1)
print(f'O antecessor do número \033[35m{valor}\033[m é \033[32m{antecessor}\033[m e seu sucessor é \033[32m{sucessor}\033[m')
