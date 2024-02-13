from time import sleep
n1 = int(input('Primeiro Número: '))
n2 = int(input('Segundo Número: '))
opção = 0
while opção != 5:
    print('''          [ 1 ] Somar
          [ 2 ] Multiplicar
          [ 3 ] Maior
          [ 4 ] Novos Números
          [ 5 ] Sair do Programa''')
    opção = int(input('Qual sua opção?: '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é igual á {}'.format(n1, n2, soma))
        print('-='*10)
        sleep(3)
    elif opção == 2:
        Multiplicação = n1 * n2
        print('A multiplicação entre {} e {} é igual á {}'.format(n1, n2, Multiplicação))
        print('-='*10)
        sleep(3)
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior número é {}'.format(maior))
        print('-='*10)
        sleep(3)
    elif opção == 4:
        print('Quais os novos número?')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
        print('-='*10)
        sleep(3)
    elif opção == 5:
        print('Finalizando...')
        print('-='*10)
        sleep(1)
        print('Fim do programa. Volte sempre!')
    else:
        print('Opção inválida. Tente novamente')
        print('-='*10)
        sleep(2)