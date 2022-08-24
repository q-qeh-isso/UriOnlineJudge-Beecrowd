while True:
    t = int(input())
    if t == 0:
        break

    for i in range(t):
        n = int(input())
        if (n - 1) % 2 == 0:
            pedidos = (n - 1) * 2 + 1
        elif (n - 1) % 2 != 0:
            pedidos = (n - 2) * 2 + 2

        print(pedidos)
