#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('digite o primeiro segmento: '))
r2 = float(input('digite o segundo segmento: '))
r3 = float(input('digite o terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os segmentos podem formar um triangulo')
else:
    print('os segmentos nao podem formar um triangulo')