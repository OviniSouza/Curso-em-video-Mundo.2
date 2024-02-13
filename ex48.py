#acumulador - Soma dos múltiplos
soma = 0
#contador - Vai mudar a cada vez q passar por um múltiplo de 3
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
            #tmb pode ser soma += 1, ou seja, soma + ela mesma + 1
        soma = soma + c
print('A soma de todos os {} números é {}'.format(cont, soma))