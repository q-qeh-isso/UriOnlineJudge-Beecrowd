while True:
    try:
        xF, yF, xI, yI, vI, r1, r2 = [int(i) for i in input().split()]

        if r1 + r2 >= ((((xI - xF) ** 2) + ((yI - yF) ** 2)) ** 0.5) + (1.5 * vI):
            print('Y')
        else:
            print('N')

    except EOFError:
        break
