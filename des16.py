#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math
num = float(input('digite um numero qualquer: '))
numero = math.trunc(num) #trunc corta o numero
print(numero)
#print(f'{int(num)}')