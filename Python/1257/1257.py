n = int(input())

for k in range(n):
    l = int(input())

    res = 0
    idx = 0
    for h in range(l):
        sent = input()
        for u in range(len(sent)):
            res += (ord(sent[u]) - 65) + h + u

        idx += 1

    print(res)
