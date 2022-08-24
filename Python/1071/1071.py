X = int(input())
Y = int(input())

total = 0

if(X > Y):
    maiorNumero = X
    X = Y
    Y = maiorNumero

for i in range(X + 1, Y):
    if(i % 2 != 0):
        total += i

print(total)
