a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
triangulo = False
if((abs(b - c) < a < b + c) and (abs(a - c) < b < a + c) and (abs(a - b) < c < a + b)):
    triangulo = True

if(triangulo):
    print(f'Perimetro = {a + b + c:.1f}')
else:
    print(f'Area = {((a + b) * c) / 2:.1f}')
