# Exercício 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome da cidade: ').lower().strip())
print(f'Nessa cidade tem Santo no nome? {'santo' in cidade}')
