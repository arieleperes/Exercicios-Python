# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = (input('digite uma frase: ')).strip().upper()

print(f'a letra A aparece {frase.count('A')} vezes')
print(f'a letra A apareceu pela primeira vez na posição {frase.find("A")+1}') # find busca pelo inicio e pega a primeira que achar
print(f'a ultima letra A apareceu na posição {frase.rfind("A")+1}') #busca do final pro começo