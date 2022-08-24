while True:
    try:
        n = input().lower().split()
    except EOFError:
        break

    qtd = 0
    i = 0
    while i < len(n):
        repete = False
        for k in range(i + 1, len(n)):
            if n[k][0] == n[i][0]:
                repete = True
                i = k
            else:
                break

        if repete:
            qtd += 1
        else:
            i += 1

    print(qtd)
