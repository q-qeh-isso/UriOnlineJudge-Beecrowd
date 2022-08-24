while True:
    try:
        n, aMin, aMax = [int(x) for x in input().split()]

        aptos = 0
        for i in range(n):
            altura = int(input())
            if aMin <= altura <= aMax:
                aptos += 1

        print(aptos)
    except EOFError:
        break
