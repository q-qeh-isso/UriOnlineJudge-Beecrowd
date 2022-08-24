n = int(input())
k = int(input())
pontos = []
for i in range(n):
    p = int(input())
    pontos.append(p)

pontos.sort(reverse=True)
qtd = 0
if k == 1 and n == 1:
    qtd += 1
elif n == 2:
    if pontos[0] == pontos[i]:
        qtd += 2
else:
    lastP = pontos[k - 1]
    qtd += k
    ct = pontos[k:].count(lastP)
    qtd += ct

print(qtd)
