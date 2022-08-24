a, b = [float(x) for x in input().split()]
aumento = ((b - a) / a) * 100
print(f'{aumento:.2f}%')
