lados = [int(x) for x in input().split()]
lados.sort()
a = lados[0]
b = lados[1]
c = lados[2]
msg = 'Invalido'
if a + b > c:
    if a != b and a != c and b != c:
        msg = 'Valido-Escaleno'
    elif ((a == b and a != c) or 
            (a == c and a != b) or
            (b == c and b != a)):
        msg = 'Valido-Isoceles'
    elif a == b and a == c:
        msg = 'Valido-Equilatero'

    print(msg)
    if c ** 2 == (a ** 2) + (b ** 2):
        print('Retangulo: S')
    else:
        print('Retangulo: N')
else:
    print(msg)
