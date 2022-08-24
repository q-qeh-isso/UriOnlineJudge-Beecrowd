while True:
    try:
        c = int(input())
        for i in range(c):
            n, m = map(int, input().split())
            res = len(str(n ** m))
            print(res)

    except EOFError:
        break
