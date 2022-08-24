from math import ceil
v, n = map(int, input().split())
t = v * n
placas = []
for i in range(10, 100, 10):
    val = ceil(float((t * i) / 100))
    placas.append(int(val))

print(*placas)
