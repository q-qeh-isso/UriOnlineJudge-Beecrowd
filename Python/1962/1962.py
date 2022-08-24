n = int(input())

for i in range(n):
    ano = int(input())
    ano -= 2015
    if ano > 0:
        print(f'{ano + 1} A.C.')
    elif ano < 0:
        print(f'{abs(ano)} D.C.')
    else:
        print('1 A.C.')
