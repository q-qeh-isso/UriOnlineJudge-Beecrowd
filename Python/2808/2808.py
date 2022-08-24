h, tg = input().split()

hR = int(h[1])
hC = h[0]
tgR = int(tg[1])
tgC = tg[0]

colunas = 'a b c d e f g h'.split()
hC = colunas.index(hC) + 1
tgC = colunas.index(tgC) + 1
if ((abs(hR - tgR) == 1 and abs(hC - tgC) == 2) or 
    (abs(hR - tgR) == 2 and abs(hC - tgC) == 1)):
    print('VALIDO')
else:
    print('INVALIDO')
