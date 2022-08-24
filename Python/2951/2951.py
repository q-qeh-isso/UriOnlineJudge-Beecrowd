n, g = map(int, input().split())
runas = []
for i in range(n):
    runas.append(input())
x = int(input())
xr = input().split()
qtd = 0
for i in xr:
    for k in runas:
        if i == k.split()[0]:
            val = int(k.split()[1])
            qtd += val
            break

print(qtd)
if qtd >= g:
    print('You shall pass!')
else:
    print('My precioooous')
