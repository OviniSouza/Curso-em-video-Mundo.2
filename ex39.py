from datetime import date
print('=-'*20)
print('DATA DE ALISTAMENTO')
print('=-'*20)

ano = int(input('Digite o ano do seu nascimento: '))
hoje = date.today().year
idade = hoje - ano

if idade < 17:
    tempo = 18 - idade
    data = hoje + tempo
    print('Se você ainda tem {} anos, ainda falta(m) {} ano(s) para que você precise se alistar. Sendo assim, você deve se apresentar no quartel em {}'.format(idade, tempo, data))

elif idade > 18:
    tempo = idade - 18
    data = hoje - tempo
    print('Se você tem {} anos, você deveria ter se alistado há {} anos, ou seja, no ano de {}. Apresente-se no quartel para se colocar em dia com urgência!'.format(idade, tempo, data))
else:
    print('Se você tem {} anos de idade, já esta na hora de se alistar no exército. Apresente-se no quartel com a documentação exigida no site gov.br'.format(idade))