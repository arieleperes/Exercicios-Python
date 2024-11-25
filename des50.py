# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0
for n in range(6):
    num = int(input('digite um numero: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'a soma de {cont} numeros pares é {soma}')


