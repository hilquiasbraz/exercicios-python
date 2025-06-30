# Exercício 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

altura = float(input('Digite a altura da parede a ser pintada, em metros: '))
largura = float(input('Digite a largura da parede a ser pintada, em metros: '))
tinta = (altura * largura) / 2
print(f'A parede tem um total de \033[32m{altura * largura:.1f} M²\033[m e necessitará de \033[32m{tinta:.1f} L\033[m de tinta')
