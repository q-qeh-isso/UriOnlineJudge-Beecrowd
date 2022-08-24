while True:
    try:
        n = int(input())
        votos = [int(x) for x in input().split()]
        aFavor = 0
        for i in votos:
            if i == 1:
                aFavor += 1

        if aFavor >= (n / 3) * 2:
            print('impeachment')
        else:
            print('acusacao arquivada')

    except EOFError:
        break
