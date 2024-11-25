# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
angulo = float(input('digite o angulo: '))
anguloR = math.radians(angulo)

seno = math.sin(anguloR)
cosseno = math.cos(anguloR)
tangente = math.tan(anguloR)

print(f'seno: {seno:.2f} / cosseno: {cosseno:.2f} / tangente: {tangente:.2f}')