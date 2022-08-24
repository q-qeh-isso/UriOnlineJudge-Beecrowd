n = int(input())
foo = 1
bar = 1
for i in range(n):
    if i == 0 and i != n - 1:
        print('0 ', end='')
    elif i == 0:
        print('0')
    elif i <= 2:
        print('1 ', end='')
    elif i == n - 1:
        print(f'{foo + bar}')
    else:
        print(f'{foo + bar} ', end='')
        temp = foo
        foo += bar
        bar = temp
