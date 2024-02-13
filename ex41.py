from datetime import date

ano = int(input('Digite o ano no qual nasceu: '))
hoje = date.today().year
idade = hoje - ano

if idade <= 9:
    print('Você tem {} anos, portanto está na categoria MIRIM'.format(idade))
elif idade > 9 and idade <= 14:
    print('Você tem {} anos, portanto está na categoria INFANTIL'.format(idade))
elif idade > 14 and idade <= 19:
    print('Você tem {} anos, portanto está na categoria JUNIOR'.format(idade))
elif idade > 19 and idade <= 20:
    print('Voce tem {} anos, portanto está na categoria SÊNIOR'.format(idade))
else:
    print('Você tem {} anos, portanto está na categoria MASTER'.format(idade))