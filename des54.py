# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime

atual = datetime.date.today().year
soma = 0
for i in range(7):
    anonascimento = int(input('digite o ano que voce nasceu: '))
    if atual - anonascimento >= 21:
        soma += 1
print(f'a quantidade de pessoas maiores que 21 anos é {soma}')