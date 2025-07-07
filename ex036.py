# Exercício 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Qual o valor da casa que você gostaria de comprar? R$ '))
salario = float(input('Qual o seu salário mensal? R$ '))
tempo = int(input('Em quantos anos você gostaria de pagar este empréstimo? '))
tempo = tempo * 12
parcela = (valor_casa / tempo)
porcentagem = salario * (30 / 100)
if parcela > porcentagem:
    print(f'Seu empréstimo foi NEGADO! A prestação de R$ {parcela:.2f} é maior que 30% do seu salário ')
else:
    print('Seu empréstimo foi APROVADO!')
