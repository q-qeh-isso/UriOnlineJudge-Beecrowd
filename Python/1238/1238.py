while True:
    try:
        n = int(input())

        for i in range(n):
            a, b = input().split()

            new = ''
            if len(a) <= len(b):
                for k in range(len(a)):
                    new += a[k] + b[k]
                if len(a) != len(b):
                    new += b[len(a):]
            elif len(a) > len(b):
                for k in range(len(b)):
                    new += a[k] + b[k]
                new += a[len(b):]

            print(new)

    except EOFError:
        break
