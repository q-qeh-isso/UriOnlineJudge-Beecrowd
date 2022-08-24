C = int(input())
T = input()
M = [[0] * 12] * 12
total = 0.0

for i in range(12):
    for k in range(12):
        M[i][k] = input()
        if(k == C):
            total += float(M[i][k])

if(T == 'S'):
    print(f'{total:.1f}')
elif(T == 'M'):
    media = total / 12
    print(f'{media:.1f}')
