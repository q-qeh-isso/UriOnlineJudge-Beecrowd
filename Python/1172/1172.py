X = []
for i in range(10):
    X.append(int(input()))

for b in range(len(X)):
    if(X[b] <= 0):
        X[b] = 1

    print(f'X[{b}] = {X[b]}')
