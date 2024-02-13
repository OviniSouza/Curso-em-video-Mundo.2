#lembrar que python conta 1 a menos sempre
for a in range(0, 6):
    print(a)
print('fim')

#O -1 vai fazer contar de trás pra frente
for b in range(6,0, -1):
    print(b)

#Vai contar de 1 a 6 de 2 em 2
for c in range(0, 7, 2):
    print(c)

#Vai fazer a contagem até o número q enviar no input
n = int(input('Digite um número: '))
for d in range(0, n + 1):
    print(d)
print('FIM')

#Passo vai dizer de quanto em quanto vai contar
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo(s): '))
for e in range(i, f+1, p):
    print(e)
print('FIM')

#Vai repetir varias vezes o input
for f in range(0, 3):
    n = int(input('Digite um valor: '))
print('FIM')

#Vai somar os valores atribuidos aos n's
s = 0
for g in range(0, 4):
    n = int(input('Digite um valor: '))
    s = s + n
print('A soma desses valores é igual a {}'.format(s))