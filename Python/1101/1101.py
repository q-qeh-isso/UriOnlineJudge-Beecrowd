while True:
    m, n = [int(i) for i in input().split()]
    soma = 0

    if m <= 0 or n <= 0:
        break
    elif m > n:
        temp = m
        m = n
        n = temp

    for i in range(m, n + 1):
        soma += i
        if i < n:
            print(f'{i} ', end='')
        else:
            print(f'{i} Sum={soma}')
