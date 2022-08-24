n = int(input())
values = []
for i in range(n):
    values.append(input())

gasto = 0
verba = 0
for i in values:
    ent, val = i.split()
    val = int(val)
    if ent == 'G':
        gasto += val
    elif ent == 'V':
        verba += val

if verba >= gasto:
    print('A greve vai parar.')
else:
    print('NAO VAI TER CORTE, VAI TER LUTA!')
