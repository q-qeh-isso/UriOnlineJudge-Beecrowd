# import math
x1, y1 = [float(L1) for L1 in input().split()]
x2, y2 = [float(L2) for L2 in input().split()]
# SEM modulo math
distancia = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1 / 2)
# COM modulo math
# distancia = math.sqrt( ((x2 - x1) ** 2) + ((y2 - y1) ** 2) )
print(f'{distancia:.4f}')
