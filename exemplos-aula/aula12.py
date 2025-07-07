# nome = str(input('Qual é o seu nome? '))
# if nome == 'Hilquias':
#     print('Que nome bonito!')
# elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
#     print('Seu nome é bem popular no Brasil!')
# elif nome in 'Ana Cláudia Jéssica Juliana':
#     print('Belo nome feminino!')
# else:
#     print('Seu nome é bem normal.')
# print(f'Tenha um bom dia, {nome}!')

# Uns testes meus para treinar minha criatividade e lógica.

import sys
print('-=-' * 6)
print('\033[45mJogo dos acordes\033[m')
print('-=-' * 6)
inicio = str(input('Você está preparado para iniciar o jogo? (Digite \033[32m1\033[m para \033[32mSIM\033[m e \033[31m0\033[m para \033[31mNÃO\033[m) '))
notas_acordes = ['c', 'd', 'e', 'f', 'g', 'a', 'b', 'f#']
notas_encontradas = []
do = 'C'.upper()
re = 'D'.upper()
mi = 'E'.upper()
fa = 'F'.upper()
sol = 'G'.upper()
la = 'A'.upper()
si = 'B'.upper()
fas = 'F#'.upper()
if inicio == '1':
    print('Então vamos lá! ')
else:
    print('Então tudo bem. Quando quiser jogar, basta apenas iniciar o programa novamente.')
    sys.exit()

print('1 - Quais as notas para formar o acorde de Dó? (Utilize a notação de cifras) ')
nota1 = str(input('Digite a primeira nota: ')).upper()
nota2 = str(input('Digite a segunda nota: ')).upper()
nota3 = str(input('Digite a terceira nota: ')).upper()
if nota1 == do or nota1 == mi or nota1 == sol and nota1 not in notas_encontradas:
    notas_encontradas.append(nota1)
    if nota2 not in notas_encontradas and nota2 == do or nota2 == mi or nota2 == sol:
        notas_encontradas.append(nota2)
    if nota3 not in notas_encontradas and nota3 == do or nota3 == mi or nota3 == sol:
        notas_encontradas.append(nota3)
else:
    print('Tá errado')

# acordes = str(input('2 - Qual a próxima nota? ')).upper()
# if acordes == do or acordes == mi or acordes == sol:
# acordes = str(input('3 - Qual a última nota? ')).upper()
# if acordes == do or acordes == mi or acordes == sol:
# print('Sua resposta está correta!')
#     else:
#         print('Sua resposta está errada!')
# else:
#     print('Então tudo bem. Quando quiser jogar, basta apenas iniciar o programa novamente.')
#     sys.exit()

# acordes = str(input('2 - Quais as notas para formar o acorde de Ré? (Utilize a notação de cifras) ')).upper()
# if acordes == re or acordes == fas or acordes == la:
#     acordes = str(input('Qual a próxima nota? ')).upper()
#     if acordes == re or acordes == fas or acordes == la:
#         acordes = str(input('Qual a última nota? ')).upper()
#         if acordes == re or acordes == fas or acordes == la:
#             print('Sua resposta está correta!')
# else:
#     print('Sua resposta está errada!')
