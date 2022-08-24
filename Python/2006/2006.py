t = int(input())
r = [int(x) for x in input().split()]
qtd = 0
for i in r:
    if i == t:
        qtd += 1

print(qtd)
