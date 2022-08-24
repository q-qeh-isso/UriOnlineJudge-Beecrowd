n = int(input())
jogos = []
for i in range(n):
    jogo = []
    L = []
    for k in range(0, 9):
        L = [int(x) for x in input().split()]
        jogo.append(L)

    jogos.append(jogo)

for i in range(len(jogos)):
    semSolucao = False
    for r in range(len(jogos[i])):
        temp = set(jogos[i][r])
        if(len(temp) != 9):
            semSolucao = True
            break

    if(not semSolucao):
        for ce in range(len(jogos[i][0])):
            col = []
            for cc in range(len(jogos[i])):
                col.append(jogos[i][cc][ce])

            colSet = set(col)
            if(len(colSet) != 9):
                semSolucao = True
                break

    if(not semSolucao):
        for q in range(0, len(jogos[i]), 3):
            quad = []
            for qb in range(0, len(jogos[i][q]), 3):
                quad = []
                quad.append(jogos[i][q][qb])
                quad.append(jogos[i][q][qb + 1])
                quad.append(jogos[i][q][qb + 2])
                quad.append(jogos[i][q + 1][qb])
                quad.append(jogos[i][q + 1][qb + 1])
                quad.append(jogos[i][q + 1][qb + 2])
                quad.append(jogos[i][q + 2][qb])
                quad.append(jogos[i][q + 2][qb + 1])
                quad.append(jogos[i][q + 2][qb + 2])

                quadSet = set(quad)
                if(len(quadSet) != 9):
                    semSolucao = True
                    break

            if(semSolucao):
                break

    print(f'Instancia {i + 1}')
    if(not semSolucao):
        print('SIM')
    else:
        print('NAO')
    print('')
