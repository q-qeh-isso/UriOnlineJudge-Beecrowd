n = int(input())
for i in range(n):
    m = int(input())
    lst = [int(x) for x in input().split()]
    odds = []
    new = []
    lst.sort(reverse=True)

    for k in range(len(lst)):
        if lst[k] % 2 != 0:
            odds.append(lst[k])

    if len(odds) != 0:
        if len(odds) % 2 == 0:
            to = len(odds) // 2
        else:
            to = len(odds) // 2 + 1
        for k in range(to):
            if len(odds) % 2 == 0:
                new.append(odds[k])
                new.append(odds[-(k + 1)])
            else:
                if k == len(odds) // 2:
                    new.append(odds[k])
                else:
                    new.append(odds[k])
                    new.append(odds[-(k + 1)])

    print(*new, sep=' ')
