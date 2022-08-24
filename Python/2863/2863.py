while True:
    try:
        t = int(input())
        menor = 0
        for i in range(t):
            e = float(input())
            if i == 0:
                menor = e
            if e < menor:
                menor = e

        print(menor)

    except EOFError:
        break
