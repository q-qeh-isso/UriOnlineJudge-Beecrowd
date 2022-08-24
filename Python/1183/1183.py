O = input()
M = []
total = 0.0
digitos = 0
for i in range(12):
    row = []
    for k in range(12):
        row.append(float(input()))
        if(k > i):
            total += row[k]
            digitos += 1
    M.append(row)

# print(total)
if(O == 'S'):
    print(f'{total:.1f}')
elif(O == 'M'):
    media = total / digitos
    print(f'{media:.1f}')
