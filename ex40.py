print('~'*20)
print('APROVADO, RECUPERAÇÃO OU REPROVADO?!')
print('~'*20)

n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))

média = (n1 + n2) / 2
verm = '\033[31m'
verd = '\033[32m'
sub = '\033[:4m'

if média < 5.0:
    print('Sua média é {}. Você está {}REPROVADO'.format(média, verm))
elif média >= 7.0:
    print('Sua média é {}. Parabéns, você foi {}APROVADO'.format(média, verd))
else:
    print('Sua média é {}. Você está de {}RECUPERAÇÃO'.format(média, sub))
