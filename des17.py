# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math
Ca = (float(input('digite o valor do cateto adjacente:')))
Co = (float(input('digite o valor do cateto oposto: ')))
hipotenusa = math.hypot(Ca,Co)
#hipotenusa = (Ca**2 + Co**2) ** (1/2)
print(f'o valor da hipotenusa é {hipotenusa:.2f}')