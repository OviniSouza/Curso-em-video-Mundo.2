print(' ')
print('CALCULADORA DE IMC')
print(' ')

p = float(input('Digite seu peso em Kg: '))
h = float(input('Digite a sua altura em m: '))

IMC = p / (h ** 2)

if IMC < 18.5:
    print('Abaixo do peso. Seu IMC é igual a {:.1f}'.format(IMC))
elif IMC >= 18.5 and IMC <= 25:
    print('Peso ideal. Seu IMC é igual a {:.1f}'.format(IMC))
elif IMC >= 25 and IMC <= 30:
    print('Sobrepeso. Seu IMC é igual a {:.1f}'.format(IMC))
elif IMC >= 30 and IMC <= 40:
    print('Obesidade. Seu IMC é igual a {:.1f}'.format(IMC))
else:
    print('Obesidade mórbida. Seu IMC é igual a {:.1f}'.format(IMC))