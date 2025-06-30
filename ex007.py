# Exercício 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

print('\033[31m=\033[m' * 30)
print('\033[30;41mDiário eletrônico de médias\033[m')
print('\033[31m=\033[m' * 30)
nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Agora digite a segunda nota do aluno: '))
media = (nota1 + nota2) / 2
print(f'A média das notas do aluno nos dois bimestres é de {media :.2f}')
