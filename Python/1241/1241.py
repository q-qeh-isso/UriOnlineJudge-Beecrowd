while True:
    try:
        n = int(input())
    except EOFError:
        break

    for i in range(n):
        a, b = input().split()

        res = 'nao encaixa'
        if len(b) <= len(a):
            aSlc = a[len(a) - len(b):]
            if aSlc == b:
                res = 'encaixa'

        print(res)
