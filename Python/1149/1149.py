linha = input().split()
a = 0
n = 0
soma = 0
for i in range(len(linha)):
    if i == 0:
        a = int(linha[i])
    else:
        if int(linha[i]) > 0:
            n = int(linha[i])
            break

for i in range(n):
    soma += a
    a += 1

print(soma)
