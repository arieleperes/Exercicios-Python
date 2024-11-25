#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('digite um ano e descubra se ele é bissexto: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('é um ano bissexto')
else:
    print('nao é bissexto')