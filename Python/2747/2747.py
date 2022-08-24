for i in range(7):
    for k in range(39):
        if i == 0 or i == 6:
            print('-' * 39)
            break
        if k == 0 or k == 38:
            if k == 38:
                print('|')
            else:
                print('|', end='')
        else:
            print(' ', end='')
