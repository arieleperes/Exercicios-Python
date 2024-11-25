#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('digite o valor do seu salario: '))

if salario <= 1250:
    novo = salario + (salario * 0.15)
    print(f'o novo salario é {novo}')
else:
    novo = salario + (salario * 0.10)
    print(f'o novo salario é {novo}')
