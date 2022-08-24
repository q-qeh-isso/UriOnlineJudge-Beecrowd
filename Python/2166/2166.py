n = int(input())
k = 0
raizInt = int(2 ** 0.5)
raizFlt = 2 ** 0.5
calc = int((1 / (raizFlt - raizInt)) * ((raizFlt + raizInt) / (raizFlt + raizInt)))

if n == 0:
    k = 1.0000000000
elif n == 1:
    k = 1.5000000000

for i in range(2, n + 1):
    if i == 2:
        k = 1 / (calc + (1 / calc))
    else:
        k = 1 / (calc + k)

if n != 0 and n != 1:
    k += 1

print(f'{k:.10f}')
