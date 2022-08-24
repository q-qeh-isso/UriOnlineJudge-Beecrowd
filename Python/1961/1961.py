P, N = input().split()
P = int(P)
N = int(N)
canos = list(input().split())
result = 'YOU WIN'
for i in range(len(canos)):
    if(i != len(canos) - 1):
        if(abs(int(canos[i]) - int(canos[i + 1])) > P):
            result = 'GAME OVER'

print(result)
