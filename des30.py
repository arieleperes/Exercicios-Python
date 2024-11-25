#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('digite um numero: '))

if (numero % 2) == 0:
    print('é par')
else:
    print('é impar')