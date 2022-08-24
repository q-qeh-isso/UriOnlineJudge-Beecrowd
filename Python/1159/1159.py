while True:
    x = int(input())
    if x == 0:
        break

    soma = 0
    pares = 0
    while pares < 5:
        if x % 2 == 0:
            soma += x
            pares += 1
        x += 1
    print(soma)
