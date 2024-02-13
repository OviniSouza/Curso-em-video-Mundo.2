print('-='*20)
print('LOJA SUPER BARATÃO')
print('-='*20)

totc = mil = menor = cont = 0
barato = ' '
while True:
    prod = str(input('Nome do produto: '))
    preço = int(input('Preço: R$'))
    totc += preço
    cont += 1
    if preço > 1000:
        mil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = prod
    resp = str(input('Quer continuar? ')).strip().upper()[0]
    if resp in 'Nn':
        break
print(f'O total da compra foi R${totc}')
print(f'Temos {mil} produtos custando mais de R$1000,00')
print(f'O produto mais barato é {barato} que custa R${menor:.2f}')