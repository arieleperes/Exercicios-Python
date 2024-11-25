#O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

nome1 = (input('digite um nome: '))
nome2 = (input('digite um nome: '))
nome3 = (input('digite um nome: '))
nome4 = (input('digite um nome: '))

lista =[nome1,nome2,nome3,nome4]
random.shuffle(lista)

print(f'o aluno escolhido foi: {lista}')