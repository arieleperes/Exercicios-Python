#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = input('digite uma frase: ').strip().split()
fraseI = ''.join(frase)
print(f'{ fraseI[0::]} , {fraseI[::-1]}')

if fraseI[0::] == fraseI[::-1]:
    print('é palindromo ')
else:
    print('Não é palindromo')

