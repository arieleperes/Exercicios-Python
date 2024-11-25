#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais

n = int(input('digite um valor: '))
n2 = int(input('digite outro valor: '))

if n > n2:
    print(f'{n} é maior que {n2}')
elif n2 > n:
    print(f'{n2} é maior que {n}')
elif n == n2:
    print('os dois valores sao iguais')