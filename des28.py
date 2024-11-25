#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
numero_aleatorio = random.randint(0,5)
numero_usuario = int(input('tente descobrir o numero escolhido pelo computador de 0 a 5: '))

if numero_aleatorio == numero_usuario:
    print('parabens! voce acertou!')
else:
    print(f'voce errou, o numero era {numero_aleatorio}')