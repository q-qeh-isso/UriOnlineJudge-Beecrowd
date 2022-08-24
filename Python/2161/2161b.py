n = int(input())
k = 0
raizInt = int(10 ** 0.5)
raizFlt = 10 ** 0.5
calc = int((1 / (raizFlt - raizInt)) * ((raizFlt + raizInt) / (raizFlt + raizInt)))

if n == 0:
    k = 0.0000000000
if n == 1:
    k = 0.1666666667

for i in range(2, n + 1):
    if i == 2:
        k = 1 / (calc + (1 / calc))
    else:
        k = 1 / (calc + k)

k += 3
print(f'{k:.10f}')
