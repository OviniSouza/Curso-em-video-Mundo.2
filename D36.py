valor = float(input('Qual o valor da casa? '))
salario = float(input('Quanto você recebe de salário? '))
tempo = int(input('Em quantos anos vai pagar a casa? '))

prestacao = valor / (tempo * 12)
maximo = 0.30 * salario

if prestacao > maximo:
    print('O valor das prestações da casa é de R${}, que excede 30% do seu sálario (R${}). Portanto, não sera possível realizar a compra da mesma! '.format(prestacao, maximo))
else:
    print('O valor das prestações da sua casa para que a mesma seja paga em {} anos é de R${}'.format(tempo, prestacao))
