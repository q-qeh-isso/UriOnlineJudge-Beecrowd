T = int(input())
N = []
w = 0
while(w < 1000):
    for i in range(T):
        if(len(N) > 999):
            break
        else:
            N.append(i)
            w += 1

for c in range(len(N)):
    print(f'N[{c}] = {N[c]}')
