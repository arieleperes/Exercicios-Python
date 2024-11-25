# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

pesoMenor = 0
pesoMaior= 0
for pessoa in range(5):
    peso = int(input('digite seu peso: '))
    if pessoa == 1:
        pesoMenor = peso
        pesoMaior = peso
    else:
        if peso > pesoMaior:
            pesoMaior = peso
        if peso < pesoMenor:
            pesoMenor = peso
print(f'o peso menor é {pesoMenor} e o peso maior é {pesoMaior}')