n = int(input())
for i in range(n):
    x, y = [int(k) for k in input().split()]
    soma = 0
    if y < x:
        temp = x
        x = y
        y = temp
    for b in range(x + 1, y):
        if b % 2 != 0:
            soma += b

    print(soma)
