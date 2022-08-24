n, m = input().split()
n = int(n)
m = int(m)
terreno = []
for i in range(n):
    linha = [int(x) for x in input().split()]
    terreno.append(linha)

x, y = 0, 0
for i in range(1, n - 1):
    for k in range(1, m - 1):
        if(terreno[i][k] == 42 and 
            terreno[i - 1][k + 1] == 7 and terreno[i - 1][k] == 7 and 
            terreno[i - 1][k - 1] == 7 and 
            terreno[i][k + 1] == 7 and terreno[i][k - 1] == 7 and 
            terreno[i + 1][k + 1] == 7 and terreno[i + 1][k] == 7 and 
            terreno[i + 1][k - 1] == 7):
            x = i
            y = k
            break

    if x != 0 or y != 0:
        break

if x != 0 and y != 0:
    x += 1
    y += 1
print(x, y)
