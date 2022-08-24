d = int(input())
ns = [int(x) for x in input().split()]

escada = 0
if len(ns) == 1 or len(ns) == 2:
    escada = 1
else:
    i = 0
    while i < len(ns) - 1:
        q = False
        dif = ns[i] - ns[i + 1]
        for k in range(i, len(ns)):
            if k == len(ns) - 1 and ns[k - 1] - ns[k] == dif:
                i = k
                escada += 1
                q = True
                break
            elif ns[k] - ns[k + 1] != dif:
                i = k
                escada += 1
                q = True
                break

        if q:
            continue

        i += 1

print(escada)
