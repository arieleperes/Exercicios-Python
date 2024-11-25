#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = input('digite uma frase: ').strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso =''
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
if inverso == junto:
    print('é palindromo')
else:
    print('não é')
