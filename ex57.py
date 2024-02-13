sexo = str(input('Qual seu sexo? [M/F] ')).upper()
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos, por favor informe seu sexo [M/F]: '))
print('Sexo {} registrado com sucesso'.format(sexo))