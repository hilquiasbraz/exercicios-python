# Exercício 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite seu salário atual: '))
if salario <= 1250:
    print(f'Seu salário será reajustado para R$ {(salario * 15 / 100) + salario:.2f}')
else:
    print(f'Seu salário será reajustado para R$ {(salario * 10 / 100) + salario:.2f}')    
