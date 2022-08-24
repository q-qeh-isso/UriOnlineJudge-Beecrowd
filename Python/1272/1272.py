while True:
    try:
        n = int(input())

        for u in range(n):
            s = [x[0] for x in input().split()]
            # print('s =', s)
            if len(s) == 0:
                print()
            else:
                print(*s, sep='')

    except EOFError:
        break
