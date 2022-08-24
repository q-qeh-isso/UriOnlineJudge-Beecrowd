while True:
    try:
        n = int(input())

        record = 0
        recordDays = ''
        for i in range(n):
            duracao, distancia = [int(x) for x in input().split()]
            vM = distancia / duracao
            if vM > record:
                record = vM
                recordDays += str(i + 1) + ' '

        for i in recordDays.split():
            print(i)

    except EOFError:
        break
