while True:
    try:
        t = int(input())

        for i in range(t):
            n, k = map(int, input().split())
            restante = 0
            c = (n // k) + (n - (k * (n // k)))

            print(c)

    except EOFError:
        break
