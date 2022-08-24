O = input()
M = []
total = 0.0
digitos = 0
for i in range(12):
    row = []
    for k in range(12):
        row.append(float(input()))
        if(k >= 12 - i and i <= k - 1):
            total += row[k]
            digitos += 1
    M.append(row)

if(O == 'S'):
    print(f'{total:.1f}')
elif(O == 'M'):
    media = total / digitos
    print(f'{media:.1f}')
