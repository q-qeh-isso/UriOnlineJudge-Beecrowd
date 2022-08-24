l = int(input())
c = int(input())

linha = 0
if l % 2 == 0:
    if c % 2 == 0:
        linha = 1
    else:
        linha = 0
else:
    if c % 2 != 0:
        linha = 1
    else:
        linha = 0

print(linha)
