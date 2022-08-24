a, b = [int(i) for i in input().split()]
if a % b < 0:
    print(f'{(a - (a % b - b)) // b} {a % b - b}')
else:
    print(f'{a // b} {a % b}')
