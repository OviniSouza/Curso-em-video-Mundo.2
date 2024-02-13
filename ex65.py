n = 0
cont = 0
soma = 0
#n = cont = soma = 0
while n != 999:
    n = int(input('Digite um número (999 para parar): '))
    soma += n
    cont += 1
    média = (soma - 999) / (cont - 1)
print('Você digitou {} números')