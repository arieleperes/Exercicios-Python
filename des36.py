#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('digite o valor da casa: '))
salario = float(input('digite seu salario: '))
anos = int(input('digite em quantos anos quer pagar o emprestimo: '))

prestaçao = casa / (anos * 12)

if salario < prestaçao * 0.30:
    print('emprestimo nao aprovado')
else:
    print(f'emprestimo aprovado! voce pagara {prestaçao:.2f} por {anos} anos')
