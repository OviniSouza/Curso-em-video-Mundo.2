n = 0
cont = 0
soma = 0
#n = cont = soma = 0
while n != 999:
    n = int(input('Digite um número (999 para parar): '))
    soma += n
    cont += 1
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont-1, soma-999))