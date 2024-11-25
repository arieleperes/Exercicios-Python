#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('digite seu nome completo: ')).strip()
n = nome.split()

print(f'o seu primeiro nome é: {n[0]}')
print(f'seu ultimo nome é: {n[-1]}')
#len vai ler quantos srts tem em nome

