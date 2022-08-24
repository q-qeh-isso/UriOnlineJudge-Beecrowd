while True:
    try:
        h, m = [int(x) for x in input().split()]
        medidas = [float(x) for x in input().split()]

        media = sum(medidas) / len(medidas)
        qt = (h * 60) // m
        somaMedidas = 0
        for i in range(len(medidas)):
            somaMedidas += (medidas[i] - media) ** 2

        res = (somaMedidas / (qt - 1)) ** 0.5

        print(f'{res:.5f}')
    except EOFError:
        break
