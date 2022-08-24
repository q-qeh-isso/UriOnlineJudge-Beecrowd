t = int(input())
caso = 1
for i in range(t):
    try:
        conversao = input()
        rgb = [int(x) for x in input().split()]

        cEye = (rgb[0] * 0.30) + (rgb[1] * 0.59) + (rgb[2] * 0.11)
        rgb.sort()
        if conversao == 'min':
            cMin = rgb[0]
            print(f'Caso #{caso}: {int(cMin)}')
        elif conversao == 'max':
            cMax = rgb[2]
            print(f'Caso #{caso}: {int(cMax)}')
        elif conversao == 'mean':
            cMean = ((rgb[0]) + (rgb[1]) + (rgb[2])) / 3
            print(f'Caso #{caso}: {int(cMean)}')
        elif conversao == 'eye':
            print(f'Caso #{caso}: {int(cEye)}')

        caso += 1

    except EOFError:
        break
