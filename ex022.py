# Exercício 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome todo em maiúsculas é {nome.upper()}')
print(f'Seu nome todo em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(' ')} letras')
dividido = nome.split()
print(f'Seu primeiro nome tem {len(dividido[0][:])} letras')
