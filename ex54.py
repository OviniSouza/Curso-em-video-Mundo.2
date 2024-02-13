from datetime import date

atual = date.today().year
totmaior = 0
totmenor = 0
for pessoas in range(1, 8):
    nasc = int(input('Em que ano a {}º pessoa nasceu? '.format(pessoas)))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    else: 
        totmenor += 1
print('Ao todo, tivemos {} pessoas maior de idade'.format(totmaior))
print('E ao todo, tivemos {} pessoa menores de idade'.format(totmenor))