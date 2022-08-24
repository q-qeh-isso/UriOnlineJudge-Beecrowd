a, b, c, d = [int(x) for x in input().split()]

if a + b > c and b + c > a and a + c > b:  # abc
    print('S')
elif b + c > d and c + d > b and b + d > c:  # bcd
    print('S')
elif a + b > d and a + d > b and b + d > a:  # abd
    print('S')
elif a + c > d and c + d > a and a + d > c:  # acd
    print('S')
else:
    print('N')
