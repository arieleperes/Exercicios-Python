#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('digite a velocidade que estava o carro: '))

if velocidade <= 80:
    print('estava dentro do limite permitido')
else:
    multa = (velocidade - 80) * 7
    print(f'voce ultrapassou o limite! recebeu uma multa de R$ {multa:.2f}')