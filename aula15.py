
n = s = 0
while True:
    n = int(input('Digite um núemro: '))
    if n == 999:
        break
    s += n
print(f'soma = {s}')