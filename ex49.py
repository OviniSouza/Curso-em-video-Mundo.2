num = int(input('Digite um número de 1 á 10 para calcular sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, (num * c)))