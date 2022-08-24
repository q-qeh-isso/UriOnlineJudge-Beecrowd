while True:
    try:
        N, M = input().split()
        qtd = 0
        for i in range(int(N), int(M) + 1):
            iStr = str(i)
            repetido = False
            for k in range(0, len(iStr)):
                for b in range(k + 1, len(iStr)):
                    if iStr[k] == iStr[b]:
                        repetido = True
                        break
                if repetido:
                    break

            if not repetido:
                qtd += 1
        print(qtd)
    except EOFError:
        break
