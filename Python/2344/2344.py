p = int(input())
nota = ''
if p == 0:
    nota = 'E'
elif p >= 1 and p <= 35:
    nota = 'D'
elif p >= 36 and p <= 60:
    nota = 'C'
elif p >= 61 and p <= 85:
    nota = 'B'
elif p >= 86 and p <= 100:
    nota = 'A'
print(nota)
