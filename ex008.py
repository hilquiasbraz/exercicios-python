# Exercício 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

print('\033[45m-\033[m' * 25)
print('\033[45mCalculadora de conversão \033[m')
print('\033[45m-\033[m' * 25)
metros = float(input('Digite a medida em metros que você gostaria de converter: '))
centimetros = float(metros * 100)
milimetros = float(metros * 1000)
print(f'A medida de \033[33m{metros :.1f} m\033[m em centímetros equivale a \033[33m{centimetros :.1f} cm\033[m e em milímetros \033[33m{milimetros :.1f} mm\033[m')
