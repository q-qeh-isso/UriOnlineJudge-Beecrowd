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

for i in range((len(m) // 2) + 1, len(m)):
    for k in range(len(m[i])):
        if k >= len(m[i]) - i and k < i:
            result += m[i][k]
            count += 1

if o == 'M':
    result /= count

print(f'{result:.1f}')
