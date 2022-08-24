t = int(input())
for j in range(t):
    b = int(input())
    p1 = [int(x) for x in input().split()]
    p2 = [int(x) for x in input().split()]

    vGolpe1 = (p1[0] + p1[1]) / 2
    vGolpe2 = (p2[0] + p2[1]) / 2

    if p1[2] % 2 == 0:
        vGolpe1 += b
    if p2[2] % 2 == 0:
        vGolpe2 += b

    vencedor = 'Dabriel'
    if vGolpe1 > vGolpe2:
        vencedor = 'Dabriel'
    elif vGolpe1 < vGolpe2:
        vencedor = 'Guarte'
    else:
        vencedor = 'Empate'

    print(vencedor)
