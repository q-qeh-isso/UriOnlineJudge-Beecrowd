while True:
    try:
        c, n = [int(x) for x in input().split()]
        dic1 = input()
        dic2 = input()
        dicio = {}
        for i in range(len(dic1)):
            dicio[str(dic1[i])] = str(dic2[i])

        # print(dicio)
        for i in range(n):
            msg = input()
            msgFinal = ''
            for s in msg:
                letra = s
                if letra.upper() in dicio.keys():
                    if letra.isupper():
                        letra = dicio[letra.upper()]
                    else:
                        letra = dicio[letra.upper()].lower()
                elif letra.upper() in dicio.values():
                    keys = list(dicio.keys())
                    vals = list(dicio.values())
                    idx = keys[vals.index(letra.upper())]
                    if letra.isupper():
                        letra = idx
                    else:
                        letra = idx.lower()

                msgFinal += letra

            print(msgFinal)
        print()

    except:
        break
