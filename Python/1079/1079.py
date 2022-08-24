n = int(input())

for i in range(n):
    v1, v2, v3 = [float(x) for x in input().split()]
    media = ((v1 * 2) + (v2 * 3) + (v3 * 5)) / 10
    print(f'{media:.1f}')
