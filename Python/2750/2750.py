for i in range(3):
    if i == 0 or i == 2:
        print('-' * 39)
        continue

    k = 0
    while k < 39:
        if k == 0 or k == 12 or k == 22:
            print('|', end='')
        elif k == 38:
            print('|')
        elif k == 3:
            print('decimal', end='')
            k += 7
            continue
        elif k == 15:
            print('octal', end='')
            k += 5
            continue
        elif k == 25:
            print('Hexadecimal', end='')
            k += 11
            continue
        else:
            print(' ', end='')

        k += 1

dec = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
octal = ['0', '1', '2', '3', '4', '5', '6', '7', '10', '11', '12', '13', '14', '15', '16', '17']
hexad = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
for i in range(len(dec)):
    r = 0
    while r < 39:
        if r == 0 or r == 12 or r == 22:
            print('|', end='')
        elif r == 38:
            print('|')
        elif r == 6:
            if len(dec[i]) == 2:
                print(dec[i], end='')
                r += len(dec[i])
            else:
                print(f' {dec[i]}', end='')
                r += len(dec[i]) + 1
            continue
        elif r == 16:
            if len(octal[i]) == 2:
                print(octal[i], end='')
                r += len(octal[i])
            else:
                print(f' {octal[i]}', end='')
                r += len(octal[i]) + 1
            continue
        elif r == 30:
            print(hexad[i], end='')
            r += len(hexad[i])
            continue
        else:
            print(' ', end='')

        r += 1

print('-' * 39)
