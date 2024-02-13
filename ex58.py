import random

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
e = random.choice(lista)

quantp = 0
acertou = False
while not acertou:
    quantp += 1
    palpite = int(input('Qual seu palpite? '))
    if palpite == e:
        acertou = True
    else:
        if palpite < e:
            print('Mais... Tente novamente!')
        elif palpite > e:
            print('Menos... Tente novamente!')
print('Acertou com {} tentativas. Parabéns!'.format(quantp))