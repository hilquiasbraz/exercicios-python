# Exercício 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

texto = str(input('Digite uma frase: ')).strip().lower()
print(f'A letra "a" aparece {texto.count('a')} vezes no texto')
print(f'A letra "a" aparece pela primeira vez na posição {texto.find('a') + 1}')
print(f'A letra "a" aparece pela última vez na posição {texto.rfind('a') + 1}')
