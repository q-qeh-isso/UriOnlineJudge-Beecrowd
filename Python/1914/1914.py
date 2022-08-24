n = int(input())
for k in range(n):
    frase = input().split()
    n, m = [int(x) for x in input().split()]
    if (n + m) % 2 == 0:
        if frase[1] == 'PAR':
            print(frase[0])
        else:
            print(frase[-2])
    else:
        if frase[1] == 'IMPAR':
            print(frase[0])
        else:
            print(frase[-2])
