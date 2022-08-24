n = int(input())
r = 0
s = 0
c = 0
for i in range(n):
    qtd, animal = input().split()
    qtd = int(qtd)
    if animal == 'R':
        r += qtd
    elif animal == 'S':
        s += qtd
    else:
        c += qtd

pR = r * 100 / (r + s + c)
pS = s * 100 / (r + s + c)
pC = c * 100 / (r + s + c)
print(f'Total: {r + s + c} cobaias')
print(f'Total de coelhos: {c}')
print(f'Total de ratos: {r}')
print(f'Total de sapos: {s}')
print(f'Percentual de coelhos: {pC:.2f} %')
print(f'Percentual de ratos: {pR:.2f} %')
print(f'Percentual de sapos: {pS:.2f} %')
