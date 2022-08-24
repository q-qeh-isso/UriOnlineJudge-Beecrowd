nota1, nota2, nota3, nota4 = input().split()

nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)
nota4 = float(nota4)
media = 0

media = (nota1 * 2 + nota2 * 3 + nota3 * 4 + nota4 * 1) / 10
print(f'Media: {media:.1f}')

if media >= 7:
    print('Aluno aprovado.')

elif media < 5:
    print('Aluno reprovado.')

else:
    print('Aluno em exame.')

    nota5 = float(input())
    print(f'Nota do exame: {nota5:.1f}')

    media = (media + nota5) / 2

    if media >= 5:
        print('Aluno aprovado.')
        print(f'Media final: {media:.1f}')
    else:
        print('Aluno reprovado.')
