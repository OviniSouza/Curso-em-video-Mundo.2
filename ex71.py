print('-='*20)
print('{:^30}'.format('BANCO VINIZIN'))
print('-='*20)

v = int(input('Que valor você quer sacar? R$'))
total = v
céd = 50
totc = 0
while True:
    if total >= céd:
        total -= céd
        totc += 1
    else: 
        if totc > 0:
            print(f'Total de {totc} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd == 1
        totc = 0
        if total == 0:
            break
print('FIm')