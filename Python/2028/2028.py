countCase = 1
while True:
    countElem = 0
    elementos = ''
    try:
        t = int(input())
        for i in range(t + 1):
            if i == 0:
                elementos += str(i)
                countElem += 1
                continue
            for k in range(i):
                elementos += ' ' + str(i)
                countElem += 1

    except EOFError:
        break

    if countElem == 1:
        print(f'Caso {countCase}: {countElem} numero')
    else:
        print(f'Caso {countCase}: {countElem} numeros')
    print(elementos)
    print()

    countCase += 1
