o = input()
m = list()
result = 0
count = 0
for i in range(12):
    linha = []
    for k in range(12):
        foo = float(input())
        linha.append(foo)
    m.append(linha)

for i in range(len(m)):
    for k in range(i):
        if (i <= len(m) // 2 - 1) or (i >= len(m) // 2 and k < len(m[i]) - i - 1):
            result += m[i][k]
            count += 1

if o == 'M':
    result /= count

print(f'{result:.1f}')
