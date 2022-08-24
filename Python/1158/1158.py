n = int(input())
while n > 0:
    x, y = [int(i) for i in input().split()]
    soma = 0
    impares = 0
    while impares < y:
        if x % 2 != 0:
            soma += x
            impares += 1
        x += 1
    print(soma)

    n -= 1
