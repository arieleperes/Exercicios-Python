#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('digite o salario: '))
aumento = salario + (salario * 0.15)

print(f'o salario com aumento vai ser R$: {aumento:.2f}')