def showList(lst):
    for i in range(len(lst)):
        for k in range(len(lst[i])):
            if k == len(lst[i]) - 1:
                print(f'{lst[i][k]}')
            else:
                print(f'{lst[i][k]}', end='')


while True:
    try:
        n = int(input())
        if(n == 0):
            break
        m = [[3] * n for _ in range(n)]
        for i in range(0, n):
            m[i][i] = 1
            m[i][-(i + 1)] = 2

        showList(m)

    except EOFError:
        break
