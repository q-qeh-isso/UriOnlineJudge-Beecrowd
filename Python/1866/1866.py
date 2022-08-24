n = int(input())
for k in range(n):
    value = int(input())
    res = 0
    for i in range(value):
        if i % 2 == 0:
            res += 1
        else:
            res -= 1
    print(res)
