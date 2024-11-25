# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n = int(input('digite um valor em metros: '))
cm = n * 100
mm = n * 1000
print(f'{n} metros é: {cm}cm e {mm}mm')