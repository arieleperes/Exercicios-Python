#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('digite um numero: '))
dobro = n * 2
triplo = n * 3
raiz= n**(1/2)
print(f' o dobro de {n} é {dobro}, o triplo é {triplo} e a raiz quadrada é {raiz:.2f}')