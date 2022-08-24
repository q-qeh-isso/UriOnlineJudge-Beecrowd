a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

resultado = (a + b + abs(a - b)) / 2
resultado = (resultado + c + abs(resultado - c)) / 2
print(f'{int(resultado)} eh o maior')
