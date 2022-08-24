n = int(input())
tMat = ''
tNota = 0
for i in range(n):
    matricula, nota = input().split()
    nota = float(nota)

    if nota > tNota:
        tNota = nota
        tMat = matricula

if tNota >= 8:
    print(tMat)
else:
    print('Minimum note not reached')
