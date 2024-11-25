#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = int(input('digite a distancia da viagem: '))

if distancia <= 200:
    valor = distancia * 0.50
    print(f'o valor da passagem vai ser R$ {valor:.2f}')
else:
    valor = distancia * 0.45
    print(f'o valor da passagem vai ser R$ {valor:.2f}')
