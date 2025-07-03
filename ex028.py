# Exercício 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
print('-' * 25)
print('   Jogo da advinhação   ')
print('-' * 25)
advinhar = int(input('Digite um número inteiro entre 0 e 5 e pressione enter: '))
teste = randint(0, 5)
if advinhar == teste:
    print('Parabéns! Você acertou o número!')
else:
    print('Você errou. Tente novamente')
