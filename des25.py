#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = input('digite seu nome: ').strip()
print(f'o seu nome tem silva? {'SILVA' in nome.upper()}')
