while True:
    try:
        n = int(input())
    except EOFError:
        break

    s = n // 100
    if n % 100 != 0:
        s += 1

    print(s)
