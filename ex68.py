from random import randint
v = 0
while True:
    p = int(input('Digite um valor: '))
    pc = randint(0, 11)
    total = p + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar?: ')).strip().upper()[0]
    print(f'Você escolheu {p} e o computador {pc}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == I:
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'Game Over! Você venceu {v} vezes.')