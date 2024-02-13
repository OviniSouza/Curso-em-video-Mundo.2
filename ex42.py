r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 and r2 == r3:
        print('Com esses segmentos, é possível formar um triângulo EQUILÁTERO')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Com esses segmentos, é possível formar um triângulo ISÓSCELES')
    else:
        print('Com esses segmentos, é possível formar um triângulo ESCALENO')
else:
    print('Não é possível formar um triângulo com esses segmentos')