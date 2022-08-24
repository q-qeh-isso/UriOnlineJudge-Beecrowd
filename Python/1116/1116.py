n = int(input())
for i in range(n):
    x, y = [int(b) for b in input().split()]
    if y != 0:
        print(f'{x / y:.1f}')
    else:
        print('divisao impossivel')
