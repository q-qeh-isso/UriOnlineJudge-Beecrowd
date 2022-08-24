n = int(input())
t = [int(i) for i in input().split()]
menor = t[0]
idx = 0
for i in range(1, n):
    if t[i] < menor:
        menor = t[i]
        idx = i + 1

if idx == 0:
    print(idx + 1)
else:
    print(idx)
