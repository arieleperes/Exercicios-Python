i= int(input('inicio: '))
f = int(input('fim: '))
p = int(input('passo: '))

for c in range(i,f+1,p):
    print (c)
print('fim')

s = 0
for c in range(0,4):
    n = int(input('digite um valor: '))
    s += n
print(f'o somatorio dos numeros é {s}')