p = float(input('Qual o valor do produto? R$'))

metodo = int(input('''Escolha um método de pagamento:
[ 1 ] À vista dinheiro ou cheque
[ 2 ] À vista no cartão
[ 3 ] Em até 2x no cartão
[ 4 ] Em 3x ou mais no cartão
Método: '''))

if metodo == 1:
    desconto = p * (10 / 100)
    valor = p - desconto
    print('O valor total do produto é de R${:.2f} com um desconto de 10% (R${:.2f}) pela escolha do pagamento à vista em dinheiro ou cheque!'.format(valor, desconto))
elif metodo == 2:
    desconto = p * (5 / 100)
    valor = p - desconto
    print('O valor total do produto é de R${:.2f} com um desconto de 5% (R${:.2f}) pela escolha do pagamento à vista no cartão!'.format(valor, desconto))
elif metodo == 3:
    parcelas = p / 2
    print('O valor total do produto é de R${:.2f}, com duas parcelas de R${:.2f}'.format(p, parcelas))
elif metodo == 4:
    vezes = int(input('Em quantas vezes deseja pagar o produto?: '))
    juros = p * (20 / 100)
    valor = p + juros
    parcelas = valor / vezes
    print('O valor total do produto é de R${}, pagando em {} vezes, as parcelas terão um valor de R${:.2f}'.format(valor, vezes, parcelas))
else:
    print('Resposta inválida! Tente novamente escolhendo entre as opções 1, 2, 3 ou 4!')