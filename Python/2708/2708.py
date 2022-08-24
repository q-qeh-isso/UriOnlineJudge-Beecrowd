jSaiu = 0
visitantes = 0
while True:
    p = [str(s) for s in input().split()]
    if p[0] == 'ABEND':
        break

    if p[0] == 'SALIDA':
        visitantes += int(p[1])
        jSaiu += 1
    elif p[0] == 'VUELTA':
        visitantes -= int(p[1])
        jSaiu -= 1

print(visitantes)
print(jSaiu)
