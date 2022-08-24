n, m = [int(x) for x in input().split()]

for i in range(m):
    acao = input()
    if acao == 'fechou':
        n += 1
    elif acao == 'clicou':
        n -= 1

print(n)
