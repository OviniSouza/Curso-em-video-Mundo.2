n = int(input('Escreva um número inteiro qualquer: '))
op = int(input('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL
Sua opção: '''))

if op == 1:
    print('{} convertído para BINÁRIO é igual a {}'.format(n, bin(n)[2:]))
elif op == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif op == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida, tente novamente.')