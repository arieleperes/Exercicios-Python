#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('digite o valor do produto: '))
novo = preço - (preço * 0.05)
print(f'na promoção vai custar R$: {novo:.2f} ')
