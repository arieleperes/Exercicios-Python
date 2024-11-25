#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO

n1 = float(input('digite sua nota: '))
n2 = float(input('digite sua outra nota: '))

media = (n1 + n2) / 2

if media > 7.0:
    print(f'{media} aprovado')
elif media > 5.0:
    print(f'{media} recuperação')
else:
    print(f'{media} reprovado')
