p, j1, j2, r, a = [int(x) for x in input().split()]
vencedor = '1'
if (j1 + j2) % 2 != 0:
    if p == 0:
        vencedor = '1'
    else:
        vencedor = '2'
else:
    if p == 1:
        vencedor = '1'
    else:
        vencedor = '2'

if a == 1:
    if r == 1:
        vencedor = '2'
    elif r == 0:
        vencedor = '1'
else:
    if r == 1:
        vencedor = '1'

print(f'Jogador {vencedor} ganha!')
