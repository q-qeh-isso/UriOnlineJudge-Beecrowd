a, b, c = [float(x) for x in input().split()]
r1 = 0
r2 = 0

raizQuad = (b ** 2) - (4 * a * c)
if(raizQuad < 0 or a == 0):
    print('Impossivel calcular')
else:
    raizQuad = raizQuad ** 0.5
    r1 = (-b + raizQuad) / (2 * a)
    r2 = (-b - raizQuad) / (2 * a)
    print(f'R1 = {r1:.5f}')
    print(f'R2 = {r2:.5f}')
