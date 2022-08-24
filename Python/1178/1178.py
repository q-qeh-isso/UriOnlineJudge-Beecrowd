x = float(input())
n = list()
for i in range(100):
    n.append(x)
    x /= 2
    print(f'N[{i}] = {n[i]:.4f}')
