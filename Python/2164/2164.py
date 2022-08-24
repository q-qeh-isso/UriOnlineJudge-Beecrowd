n = int(input())
numFibo = (((1 + (5 ** 0.5)) / 2) ** n - ((1 - (5 ** 0.5)) / 2) ** n) / (5 ** 0.5)
print(f'{numFibo:.1f}')
