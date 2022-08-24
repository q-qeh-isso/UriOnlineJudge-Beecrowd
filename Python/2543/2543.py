while True:
    try:
        n, l = [int(x) for x in input().split()]
        aFavor = 0
        gameplays = 0
        for b in range(n):
            i, j = [int(x) for x in input().split()]
            if i == l and j == 0:
                gameplays += 1

        print(gameplays)
    except EOFError:
        break
