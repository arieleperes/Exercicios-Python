# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input('digite o primeiro termo de uma PA: '))
razao = int(input('digite a razão: '))
decimo = termo + (10 -1) * razao
for n in range(termo,decimo + razao ,razao):
    print(n)