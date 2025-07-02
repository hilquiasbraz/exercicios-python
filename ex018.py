# Exercício 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tg = math.tan(math.radians(angulo))
print(f'O seno do ângulo de {angulo}º é {seno:.2f} \nSeu cosseno é {cosseno:.2f} \nE sua tangente é {tg:.2f}')
