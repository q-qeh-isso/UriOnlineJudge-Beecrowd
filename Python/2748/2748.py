for i in range(7):
    k = 0
    while k < 39:
        if i == 0 or i == 6:
            print('-' * 39)
            break
        if k == 0 or k == 38:
            if k == 38:
                print('|')
            else:
                print('|', end='')
        elif i == 1 and k == 9:
            print('Roberto', end='')
            k += 6
        elif i == 3 and k == 9:
            print('5786', end='')
            k += 3
        elif i == 5 and k == 9:
            print('UNIFEI', end='')
            k += 5
        else:
            print(' ', end='')

        k += 1
