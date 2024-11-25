#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.


altura = float(input('digite a altura da parede: '))
largura = float(input('digite a largura da parede: '))

area = altura * largura
tinta = area / 2
print(f'vai precisar de {tinta} litros de tinta ')