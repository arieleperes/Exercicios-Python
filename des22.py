#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.

nome = input('digite seu nome completo: ').strip()

print(f'seu nome com todas as letras maisculas: {nome.upper()}')
print(f'seu nome com todas as letras minusculas: {nome.lower()}')
print(f'quantas letras tem seu nome: {len(nome) - nome.count(' ')}')

nome_lista = nome.split() # vira uma lista
primeiro_nome = nome_lista[0] 
print(f'o seu primeiro nome tem letras {len(primeiro_nome)}')