#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random
nome1 = (input('digite um nome: '))
nome2 = (input('digite um nome: '))
nome3 = (input('digite um nome: '))
nome4 = (input('digite um nome: '))

lista =[nome1,nome2,nome3,nome4]
sorteio = random.choice(lista)

print(f'o aluno escolhido foi: {sorteio}')