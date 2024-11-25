# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
atual = date.today().year
ano = int(input('digite seu ano de nascimento: '))
idade = atual - ano

if idade == 18:
    print('esta na hora de se alistar')
elif idade > 18:
   tempo = idade - 18
   print(f'ja passou do tempo do alistamento, esta atrasado em {tempo} ano/anos')
elif idade < 18:
    tempo = 18 - idade
    print(f'falta {tempo} anos para se alistar')