# Exercício 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

print('\033[35m*' * 63)
print('Digite um número para saber seu dobro, triplo e raiz quadrada: ')
print('\033[35m*\033[m' * 63)
numero = int(input())
cores = {'limpa':'\033[m', 'ciano':'\033[36m', 'iversaocores':'\033[36;47m'}
print(f'{cores["ciano"]}O dobro do número {cores["iversaocores"]}{numero}{cores["limpa"]} {cores["ciano"]}é{cores["limpa"]} {cores["iversaocores"]}{numero * 2}{cores["limpa"]} \n{cores["ciano"]}Seu triplo é {cores["iversaocores"]}{numero * 3}{cores["limpa"]} \n{cores["ciano"]}E sua raiz quadrada é {cores["iversaocores"]}{numero ** (1 / 2):.1f}{cores["limpa"]}')
