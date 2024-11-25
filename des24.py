#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

nome = input('digite o nome de uma cidade').strip()
primeiro_nome = nome.split()
primeiro = primeiro_nome[0]

if primeiro == ('santo'):
    print('começa com santo')
else:
    print('nao começa com santo')

#ou
# nome = input('digite o nome de uma cidade').strip()
# print(nome[:5].upper() == 'SANTO')
