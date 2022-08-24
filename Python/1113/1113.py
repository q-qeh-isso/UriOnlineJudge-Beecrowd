while True:
    x, y = [int(i) for i in input().split()]

    if x == y:
        break
    elif x > y:
        print('Decrescente')
    else:
        print('Crescente')
