notas = [2, 5, 10, 20, 50, 100]
while True:
    n, m = [int(x) for x in input().split()]
    if n == 0 and m == 0:
        break

    troco = m - n
    notasQtd = 0
    for i in range(len(notas)):
        if troco == notas[i] * 2:
            notasQtd = 2
            print('possible')
            break

    if notasQtd == 0:
        for i in range(5, -1, -1):
            if notasQtd == 3:
                break

            if troco - notas[i] >= 0:
                troco -= notas[i]
                notasQtd += 1

        if troco == 0 and notasQtd == 2:
            print('possible')
        else:
            print('impossible')
