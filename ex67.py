while True:
    n = int(input('Qual número? '))
    if n < 0:
        break
    print('-='*10)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-='*10)
print('Programa encerrado!')