N = []
for i in range(20):
    N.append(input())

count = 0
for b in range(len(N), 0, - 1):
    print(f'N[{count}] = {N[b - 1]}')
    count += 1
