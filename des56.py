#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma = 0
cont = 0
maior= 0
nomeVelho =''
for pessoa in range(2):
    nome = input('digite seu nome: ')
    idade = int(input('digite sua idade: '))
    sexo = input('digite seu sexo (f ou m): ')
    soma += idade
    if sexo == 'f' and idade < 20:
        cont += 1
    if sexo == 'm' :
        if idade > maior:
            maior = idade


print(f'o homem mais velho tem {maior} anos')
print(f'{cont} mulheres tem menos de 20 anos')
print(f' a media de idades é {soma/4}')