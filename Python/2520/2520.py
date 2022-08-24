while True:
    try:
        n, m = [int(x) for x in input().split()]
        cidade = [[0] * m for _ in range(n)]
        # showLista(cidade)
        x1, y1, x2, y2 = 0, 0, 0, 0
        for i in range(n):
            linha = [int(x) for x in input().split()]
            for r in range(len(linha)):
                if linha[r] != 0:
                    cidade[i][r] = linha[r]
                    if linha[r] == 2:
                        x2 = i
                        y2 = r
                    else:
                        x1 = i
                        y1 = r

        seg = (abs(x2 - x1)) + (abs(y2 - y1))
        print(seg)
    except EOFError:
        break
