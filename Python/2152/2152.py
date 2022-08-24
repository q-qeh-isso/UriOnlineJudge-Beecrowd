c = int(input())
for i in range(c):
    h, m, o = input().split()
    if len(h) == 1:
        h = '0' + h
    if len(m) == 1:
        m = '0' + m
    if o == '1':
        print(f'{h}:{m} - A porta abriu!')
    elif o == '0':
        print(f'{h}:{m} - A porta fechou!')
