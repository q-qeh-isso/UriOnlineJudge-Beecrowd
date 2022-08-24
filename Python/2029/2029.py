while True:
    try:
        vol = float(input())
        diam = float(input())

        altura = vol / (3.14 * ((diam / 2) * (diam / 2)))
        area = 3.14 * (((diam / 2) * (diam / 2)))

        print(f'ALTURA = {altura:.2f}')
        print(f'AREA = {area:.2f}')

    except EOFError:
        break
