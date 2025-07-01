# Exercício 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math
catadj = float(input('Digite o comprimento do cateto adjascente: '))
catop = float(input('Digite o comprimento do cateto oposto: '))
hip = math.hypot(catadj, catop)
print(f'A hipotenusa dos catetos adjascente e oposto, de comprimento {catadj} cm e {catop} cm, respectivamente é {hip:.2f}')
