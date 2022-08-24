n = int(input())
k = 0

if n == 0:
    k = 0.0000000000
if n == 1:
    k = 0.1666666667

for i in range(2, n + 1):
    if i == 2:
        k = 1 / (6 + (1 / 6))
    else:
        k = 1 / (6 + k)

k += 3
print(f'{k:.10f}')
