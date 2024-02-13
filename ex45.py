import random
from time import sleep

print('-='*20)
print('PEDRA, PAPEL E TESOURA')
print('''Jogue pedra, papel, tesoura com o pc! 
Lembre-se de digitar a resposta corretamente e com todas as letras MINÚSCULAS
BOA SORTE!!''')
print('-='*20)

print(''' 
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
p1 = int(input('Sua escolha: '))

print('-='*11)
print('JO')
sleep(1)
print('KEN')
sleep(2)
print('PÔ')
print('-='*11)

lista = ['pedra', 'papel', 'tesoura']
pc = random.choice(lista)
verd = '\033[32m'
verm = '\033[31m'
bran = '\033[30m'
fimcor = '\033[m'

ganhou = 'O PC escolheu {}. Você {}VENCEU{}!'.format(pc, verd, fimcor)
perdeu = 'O PC escolheu {}. Você {}PERDEU{}!'.format(pc, verm, fimcor)
empate = 'O PC escolheu {}. Vocês {}EMPATARAM{}!'.format(pc, bran, fimcor)

print('''PC escolheu {}
Você escolheu {}'''.format(pc, p1))
print('-='*11)

if pc == 'pedra' and p1 == 2:
    print(ganhou)
elif pc == 'pedra' and p1 == 3:
    print(perdeu)
elif pc == 'pedra' and p1 == 1:
    print(empate)

elif pc == 'papel' and p1 == 1:
    print(perdeu)
elif pc == 'papel' and p1 == 3:
    print(ganhou)
elif pc == 'papel' and p1 == 2:
    print(empate)

elif pc == 'tesoura' and p1 == 1:
    print(ganhou)
elif pc == 'tesoura' and p1 == 2:
    print(perdeu)
elif pc == 'tesoura' and p1 == 3:
    print(empate)

else:
    print('Resposta inválida. Tente novamente escolhendo pedra, papel ou tesoura!')