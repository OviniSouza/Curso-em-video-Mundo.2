frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
#desconsidera os espaços
junto = ''.join(palavras)
#inverso = ''
inverso = junto[::-1]

#for letra in range(len(junto) -1, -1, -1):
#    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um PALÍNDROMO')
else:
    print('A frase não é um PALÍNDROMO')