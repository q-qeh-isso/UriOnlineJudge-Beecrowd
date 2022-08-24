while True:
    try:
        x, y, m = [int(x) for x in input().split()]
        # ans = []
        for i in range(m):
            d1, d2 = [int(x) for x in input().split()]

            if (x >= d1 and y >= d2) or (x >= d2 and y >= d1):
                print('Sim')
                # ans.append('Sim')
            else:
                print('Nao')
                # ans.append('Nao')

        # print(*ans, sep='\n')

    except EOFError:
        break
