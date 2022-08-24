N1, N2, N3, N4 = input().split()
N1, N2, N3, N4 = float(N1), float(N2), float(N3), float(N4)

media = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1)) / 10
print(f'Media: {media:.1f}')

result = 'Aluno reprovado.'
alunoEmExame = False
notaExame = 0

if(media >= 7.0):
    print('Aluno aprovado.')
elif(media >= 5.0 and media <= 6.9):
    print('Aluno em exame.')
    alunoEmExame = True
else:
    print('Aluno reprovado.')

if(alunoEmExame):
    notaExame = float(input())
    print(f'Nota do exame: {notaExame:.1f}')

    media = (media + notaExame) / 2

    if(media >= 5.0):
        print('Aluno aprovado.')

    print(f'Media final: {media:.1f}')
