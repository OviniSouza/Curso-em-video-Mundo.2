casa = int(input('Qual o valor da casa?: '))
salario = float(input('Qual o seu salário?: '))
anos  = int(input('Em quantos anos pretende pagar a casa?: '))
vermelho = '\033[31m'

prestação = casa / (anos*12)
if prestação <= salario * (30 / 100):
    print('O valor das prestações dessa casa é igual a R${:.2f}. Empréstimo CONCEDIDO'.format(prestação))
else:
    print('O valor das prestações, que é de R${:.2f}, excede 30% do seu salário, por esse motivo o empréstimo foi {}negado'.format(prestação, vermelho))