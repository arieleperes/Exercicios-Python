# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

graus = float(input('digite o valor da temperatura em graus Celsius: '))
conversão = (graus * 1.8) + 32

print(f'{graus} graus celsius em fahrenheit é {conversão:.2f}')