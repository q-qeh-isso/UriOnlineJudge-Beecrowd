abc = [float(x) for x in input().split()]
abcSort = sorted(abc, reverse=True)
a = abcSort[0]
b = abcSort[1]
c = abcSort[2]

if(a >= b + c):
    print('NAO FORMA TRIANGULO')
elif(a**2 == b**2 + c**2):
    print('TRIANGULO RETANGULO')
elif(a**2 > b**2 + c**2):
    print('TRIANGULO OBTUSANGULO')
elif(a**2 < b**2 + c**2):
    print('TRIANGULO ACUTANGULO')

if(a == b and a == c):
    print('TRIANGULO EQUILATERO')
elif((a == b and a != c) or (b == c and b != a) or (c == a and c != b)):
    print('TRIANGULO ISOSCELES')
