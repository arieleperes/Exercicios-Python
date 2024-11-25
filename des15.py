#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('quantos KMs foram rodados?: '))
dias = int(input('por quantos dias?: '))

pag_dias = dias * 60
pag_km = km * 0.15
total= pag_km + pag_dias

print(f'O valor a pagar é R${total:.2f}')