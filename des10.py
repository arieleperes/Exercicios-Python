#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

n = float(input('digite quanto tem na sua carteira: '))
dollar = n / 3.27
print(f'com essa quantia da para comprar {dollar:.2f} dolares')