x, y = [int(i) for i in input().split()]
dig = 1
for i in range(1, y // x + 1):
    for k in range(x):
        if k == x - 1:
            print(f'{dig}')
        else:
            print(f'{dig} ', end='')
        dig += 1
