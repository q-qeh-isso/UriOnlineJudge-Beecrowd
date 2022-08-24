N = []
N.append(int(input()))
for i in range(1, 10):
    N.append(N[i - 1] * 2)

for b in range(len(N)):
    print(f'N[{b}] = {N[b]}')
