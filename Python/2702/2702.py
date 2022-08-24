d = [int(s) for s in input().split()]
p = [int(s) for s in input().split()]

total = 0
for i in range(3):
    t = d[i] - p[i]
    if d[i] - p[i] < 0:
        total += abs(t)

print(total)
