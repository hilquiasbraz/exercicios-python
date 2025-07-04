# Exercício 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('=-' * 20)
print('Analisador de triângulos')
print('=-' * 20)
l1 = int(input('Qual o tamanho do primeiro segmento de reta? '))
l2 = int(input('Qual o tamanho do segundo segmento de reta? '))
l3 = int(input('Qual o tamanho do terceiro segmento de reta? '))
if l1 > (l2 + l3) or l2 > (l1 + l3) or l3 > (l1 + l2):
    print('Esses segmentos de reta PODEM formar um triângulo')
if l1 == l2 == l3:
    print('Esses segmentos de reta FORMAM um triângulo equilátero')
else:
    print('Esses segmentos de reta NÃO FORMAM um triângulo')
