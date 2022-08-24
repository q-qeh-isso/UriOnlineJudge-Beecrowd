def buscaAdjacentes(tabuleiro, r, c):
    parentes = []
    if tabuleiro[r][c] == 9:
        return 9
    else:
        if r == 0 and len(tabuleiro) > 1:
            if c == 0:
                parentes.append(tabuleiro[r][c + 1])
                parentes.append(tabuleiro[r + 1][c])
            elif c == len(tabuleiro[r]) - 1:
                parentes.append(tabuleiro[r][c - 1])
                parentes.append(tabuleiro[r + 1][c])
            else:
                parentes.append(tabuleiro[r + 1][c])
                parentes.append(tabuleiro[r][c - 1])
                parentes.append(tabuleiro[r][c + 1])
        elif r == 0 and len(tabuleiro) == 1:
            if c == 0:
                parentes.append(tabuleiro[r][c + 1])
            elif c == len(tabuleiro[r]) - 1:
                parentes.append(tabuleiro[r][c - 1])
            else:
                parentes.append(tabuleiro[r][c - 1])
                parentes.append(tabuleiro[r][c + 1])
        elif r == len(tabuleiro) - 1:
            if c == 0:
                parentes.append(tabuleiro[r - 1][c])
                parentes.append(tabuleiro[r][c + 1])
            elif c == len(tabuleiro[r]) - 1:
                parentes.append(tabuleiro[r - 1][c])
                parentes.append(tabuleiro[r][c - 1])
            else:
                parentes.append(tabuleiro[r - 1][c])
                parentes.append(tabuleiro[r][c - 1])
                parentes.append(tabuleiro[r][c + 1])
        else:
            if c == 0:
                parentes.append(tabuleiro[r - 1][c])
                parentes.append(tabuleiro[r][c + 1])
                parentes.append(tabuleiro[r + 1][c])
            elif c == len(tabuleiro[r]) - 1:
                parentes.append(tabuleiro[r - 1][c])
                parentes.append(tabuleiro[r + 1][c])
                parentes.append(tabuleiro[r][c - 1])
            else:
                parentes.append(tabuleiro[r - 1][c])
                parentes.append(tabuleiro[r][c + 1])
                parentes.append(tabuleiro[r + 1][c])
                parentes.append(tabuleiro[r][c - 1])

        qtd = 0
        for i in range(len(parentes)):
            if parentes[i] == 9:
                qtd += 1

        return qtd


def showLista(lista):
    for i in range(len(lista)):
        for k in range(len(lista[i])):
            if k == len(lista[i]) - 1:
                print(lista[i][k])
            else:
                print(lista[i][k], end='')


while True:
    try:
        n, m = [int(x) for x in input().split()]
        tabuleiro = []

        for i in range(n):
            row = [int(x) for x in input().split()]
            for k in range(len(row)):
                if row[k] == 1:
                    row[k] = 9
            tabuleiro.append(row)

        for i in range(len(tabuleiro)):
            for k in range(len(tabuleiro[i])):
                tabuleiro[i][k] = buscaAdjacentes(tabuleiro, i, k)

        showLista(tabuleiro)

    except EOFError:
        break
